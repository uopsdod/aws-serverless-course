import botocore.session

# Initialize the DynamoDB client
region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)

table_name = "game-python-001"
gsi_name = "gsi-vip-hour"

# Update the table to add a GSI
try:
    response = dynamodb.update_table(
        TableName=table_name,
        AttributeDefinitions=[
            {'AttributeName': 'is_vip', 'AttributeType': 'S'},  # Specify the data type for GSI partition key
            {'AttributeName': 'hour', 'AttributeType': 'N'},    # Specify the data type for GSI sort key
        ],
        GlobalSecondaryIndexUpdates=[
            {
                'Create': {
                    'IndexName': gsi_name,
                    'KeySchema': [
                        {'AttributeName': 'is_vip', 'KeyType': 'HASH'},  # GSI Partition key
                        {'AttributeName': 'hour', 'KeyType': 'RANGE'},   # GSI Sort key
                    ],
                    'Projection': {
                        'ProjectionType': 'INCLUDE',
                        'NonKeyAttributes': ['duration', 'winner', 'type']  # Fields to project into the GSI
                    },
                    # ProvisionedThroughput can be omitted for tables using on-demand capacity
                },
            },
        ],
    )
    print("GSI addition initiated. It might take some time for the GSI to become active.")
except botocore.exceptions.ClientError as error:
    print(f"Error updating table: {error}")
