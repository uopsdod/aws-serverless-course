#!/usr/bin/env python3
import botocore.session
import json
from amazondax import AmazonDaxClient

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

# DAX Cache
dax_cluster_endpoint = 'daxs://dax-cluster-demo-001.pmu19g.dax-clusters.us-east-2.amazonaws.com' 
dynamodb = AmazonDaxClient(session, endpoints=[dax_cluster_endpoint], region_name=region)

table_name = "game-python-001"

partition_key = "10"

# Using the query API with expression attribute names for both hour and type
response = dynamodb.query(
    TableName=table_name,
    KeyConditionExpression="#hour = :hour_val",
    ExpressionAttributeValues={
        ":hour_val": {"N": partition_key}
    },
    ExpressionAttributeNames={
        "#hour": "hour",  # hour is a reserved keyword in Query
    }
)

# Process the query result
items = response.get('Items', [])
if items:
    print(f"Found {len(items)} items with hour {partition_key}.")
    # for item in items:
    #     # Convert DynamoDB item to a more readable format, if needed
    #     readable_item = {
    #         "hour": item["hour"]["N"],
    #         "type": item["type"]["S"],
    #         "duration": item["duration"]["N"],
    #         "winner": item["winner"]["S"],
    #         "players": json.dumps(item["players"]["SS"]),  # Convert set to JSON string for readability
    #         "is_vip": item["is_vip"]["S"]
    #     }
    #     print("Retrieved item:", readable_item)
else:
    print(f"No items found with hour {partition_key}.")
