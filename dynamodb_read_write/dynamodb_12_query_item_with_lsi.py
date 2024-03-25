#!/usr/bin/env python3
import botocore.session
import json

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

# DAX Cache (for learning purpose)
import sys
if len(sys.argv) > 1:
    from amazondax import AmazonDaxClient
    dax_cluster_endpoint = sys.argv[1]  # Assuming the DAX endpoint is the first argument
    dynamodb = AmazonDaxClient(session, endpoints=[dax_cluster_endpoint], region_name=region)
    print("DAX in use.")

table_name = "game-python-001"
lsi_name = "lsi-duration"

# Specifying the hour and the condition for duration
partition_key_value = "12"
duration_threshold = "250" # sort key 

response = dynamodb.query(
    TableName=table_name,
    IndexName=lsi_name,
    KeyConditionExpression="#hour = :hour_val AND #duration > :duration_val",
    ExpressionAttributeValues={
        ":hour_val": {"N": partition_key_value},
        ":duration_val": {"N": duration_threshold}
    },
    ExpressionAttributeNames={
        "#hour": "hour",  # Alias for reserved keyword and also the partition key in your table and LSI
        "#duration": "duration"  # Alias for the sort key in your LSI
    }
)

# Process the query result
items = response.get('Items', [])
if items:
    print(f"Found {len(items)} items with hour {partition_key_value} and duration greater than {duration_threshold}.")
    for item in items:
        # Convert DynamoDB item to a more readable format
        readable_item = {
            "hour": item["hour"]["N"],
            "type": item["type"]["S"],
            "duration": item["duration"]["N"],
            "winner": item["winner"]["S"],
        }
        print("Retrieved item:", readable_item)
else:
    print(f"No items found with hour {partition_key_value} and duration greater than {duration_threshold}.")
