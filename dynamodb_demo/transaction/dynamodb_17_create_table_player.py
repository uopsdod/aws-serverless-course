#!/usr/bin/env python3
import botocore.session

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "game-player-001"

params = {
    'TableName' : table_name,
    'KeySchema': [       
        { 'AttributeName': "name", 'KeyType': "HASH"},    # Partition key
    ],
    'AttributeDefinitions': [       
        { 'AttributeName': "name", 'AttributeType': "S" }, # Partition key
    ],
    'BillingMode': 'PAY_PER_REQUEST',  # This enables on-demand capacity
}

# Create the table
dynamodb.create_table(**params)

# Wait for the table to exist before exiting
print('creating table', table_name, '...')
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)
print('Finished creating', table_name, '.')

