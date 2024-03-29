#!/usr/bin/env python3
import botocore.session

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
partition_key = '10'
sort_key = 'baseball'

# Define the update parameters
params = {
    'TableName': table_name,
    'Key': {
        "hour": {'N': partition_key},
        "type": {'S': sort_key}
    },
    'UpdateExpression': 'SET is_vip = :is_vip_val',
    'ExpressionAttributeValues': {
        ':is_vip_val': {'S': 'false'}
    },
}

# Perform the update
response = dynamodb.update_item(**params)
print(f"finished updating item ({partition_key}, {sort_key})")
