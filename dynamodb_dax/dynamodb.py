import boto3

# Note: This one work if you don't need DAX. DAX has no resource-style code in python to use.

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')  # Specify your region

# Reference the table
table = dynamodb.Table('game_1000')

# Get an item using its primary key
response_get = table.get_item(
    Key={
        'hour': '22',
        'type': 'baseball'
    }
)

# Print the retrieved item
item = response_get.get('Item', {})
print(f"# of returned get item: {len(item)}")

# Query the table for items 
response_query = table.query(
    KeyConditionExpression=
    boto3.dynamodb.conditions.Key('hour').eq('12') 
    & boto3.dynamodb.conditions.Key('type').eq('baseball')
)

# Print the items returned by the query
items = response_query.get('Items', [])
print(f"# of returned queried items: {len(items)}")

# Scan the table for items (be cautious with large tables)
response_scan = table.scan(
    FilterExpression=
    boto3.dynamodb.conditions.Attr('is_vip').eq('true') 
    & boto3.dynamodb.conditions.Attr('type').contains('ball')
)

# Print the items returned by the scan
items = response_scan.get('Items', [])
print(f"# of returned scanned items: {len(items)}")


