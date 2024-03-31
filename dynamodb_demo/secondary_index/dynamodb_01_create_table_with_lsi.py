#!/usr/bin/env python3
import botocore.session

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "game-python-index-001"
lsi_name = "lsi-duration"

params = {
    'TableName': table_name,
    'KeySchema': [       
        {'AttributeName': "hour", 'KeyType': "HASH"},  # Partition key
        {'AttributeName': "type", 'KeyType': "RANGE"}   # Sort key
    ],
    'AttributeDefinitions': [       
        {'AttributeName': "hour", 'AttributeType': "N"},  # Partition key
        {'AttributeName': "type", 'AttributeType': "S"},  # Sort key
        {'AttributeName': "duration", 'AttributeType': "N"}  # Additional attribute for LSI
    ],
    'BillingMode': 'PAY_PER_REQUEST',
    'LocalSecondaryIndexes': [
        {
            'IndexName': lsi_name,
            'KeySchema': [
                {'AttributeName': "hour", 'KeyType': "HASH"},  # Same partition key as the table
                {'AttributeName': "duration", 'KeyType': "RANGE"}  # Sort key for the index
            ],
            'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': ['winner','type']
            }
        }
    ]
}

# Create the table with LSI
response = dynamodb.create_table(**params)
print(f"Creating table {table_name} with LSI on 'duration' and including 'type' and 'winner' fields...")
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)
print(f"Finished creating table {table_name} with LSI.")
