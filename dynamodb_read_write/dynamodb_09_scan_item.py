#!/usr/bin/env python3
import botocore.session

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

table_name = "game-python-001"

is_vip = True

# Using the scan API with a filter expression for is_vip = True
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression="is_vip = :is_vip",
    ExpressionAttributeValues={
        ":is_vip": {"BOOL": is_vip}
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
        #     "is_vip": item["is_vip"]["BOOL"]
        # }
        # print("Retrieved item:", readable_item)
else:
    print("No items found where is_vip is True.")
