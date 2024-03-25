#!/usr/bin/env python3
import botocore.session
from amazondax import AmazonDaxClient

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

# DAX Cache
dax_cluster_endpoint = 'daxs://dax-cluster-demo-001.pmu19g.dax-clusters.us-east-2.amazonaws.com' 
dynamodb = AmazonDaxClient(session, endpoints=[dax_cluster_endpoint], region_name=region)

table_name = "game-python-001"

is_vip = 'true'

# Using the scan API with a filter expression for is_vip = True
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression="is_vip = :is_vip",
    ExpressionAttributeValues={
        ":is_vip": {"S": is_vip}
    }
)

# Process the scan result
items = response.get('Items', [])
if items:
    print(f"Found {len(items)} items where is_vip is {is_vip}.")
    # for item in items:
        # Convert DynamoDB item to a more readable format, if needed
        # readable_item = {
        #     "hour": item["hour"]["N"],
        #     "type": item["type"]["S"],
        #     "duration": item["duration"]["N"],
        #     "winner": item["winner"]["S"],
        #     "players": json.dumps(item["players"]["SS"]),  # Convert set to JSON string for readability
        #     "is_vip": item["is_vip"]["S"]
        # }
        # print("Retrieved item:", readable_item)
else:
    print(f"No items found where is_vip is {is_vip}.")
