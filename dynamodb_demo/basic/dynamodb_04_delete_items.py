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
partition_key = '12'
sort_key = 'tennis'

# Define the delete parameters
params = {
    'TableName': table_name,
    'Key': {
        "hour": {'N': partition_key},
        "type": {'S': sort_key}
    }
}

# Perform the delete
response = dynamodb.delete_item(**params)
print(f"Finished deleting item ({partition_key}, {sort_key})")
