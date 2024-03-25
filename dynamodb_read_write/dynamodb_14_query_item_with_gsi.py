#!/usr/bin/env python3
import botocore.session
import json

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

# DAX Cache
import sys
if len(sys.argv) > 1:
    from amazondax import AmazonDaxClient
    dax_cluster_endpoint = sys.argv[1]  # Assuming the DAX endpoint is the first argument
    dynamodb = AmazonDaxClient(session, endpoints=[dax_cluster_endpoint], region_name=region)

table_name = "game-python-001"
gsi_name = "gsi-vip-hour"  # Name of the GSI

# Query parameters
is_vip = "true"  # partition key
start_hour = 8 # sort key
end_hour = 16 # sort key

# Query the GSI
response = dynamodb.query(
    TableName=table_name,
    IndexName=gsi_name, 
    KeyConditionExpression="is_vip = :vip_val AND #hour BETWEEN :start_hour AND :end_hour",
    ExpressionAttributeValues={
        ":vip_val": {"S": is_vip},
        ":start_hour": {"N": str(start_hour)},
        ":end_hour": {"N": str(end_hour)}
    },
    ExpressionAttributeNames={
        "#hour": "hour",  # hour is a reserved keyword in Query
    }
)

# Process the query result
items = response.get('Items', [])
if items:
    print(f"Found {len(items)} items with is_vip {is_vip} and hour between {start_hour} to {end_hour}.")
    # for item in items:
    #     # Convert DynamoDB item to a more readable format, if needed
    #     readable_item = {
    #         "hour": item["hour"]["N"],
    #         "type": item["type"]["S"],
    #         "duration": item["duration"]["N"],
    #         "winner": item["winner"]["S"],
    #         "is_vip": item["is_vip"]["S"]
    #     }
    #     print("Retrieved item:", readable_item)
else:
    print(f"No items found with is_vip {is_vip} and hour between {start_hour} to {end_hour}.")
