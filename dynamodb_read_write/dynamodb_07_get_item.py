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

partition_key = "10"
sort_key = "baseball"

# Use get_item to fetch the specific item
response = dynamodb.get_item(
    TableName=table_name, 
    Key={
        "hour": {"N": partition_key},
        "type": {"S": sort_key}
    }
)

# Assuming you want to print the item or do something with it
item = response.get('Item')
if item:
    # Convert DynamoDB item to a more readable format, if needed
    readable_item = {
        "hour": item["hour"]["N"],
        "type": item["type"]["S"],
        "duration": item["duration"]["N"],
        "winner": item["winner"]["S"],
        "players": json.dumps(item["players"]["SS"]),  # Convert set to JSON string for readability
        "is_vip": item["is_vip"]["S"]
    }
    print("Retrieved item:", readable_item)
else:
    print(f"Item with hour {hour_to_get} and type {type_to_get} not found.")
