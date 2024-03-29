#!/usr/bin/env python3
import botocore.session

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "game-player-001"

response = dynamodb.delete_table(TableName=table_name)

# Wait for the table to be deleted before exiting
print(f'deleting {table_name}.')
waiter = dynamodb.get_waiter('table_not_exists')
waiter.wait(TableName=table_name)
print(f'Finished deleting {table_name}.')
