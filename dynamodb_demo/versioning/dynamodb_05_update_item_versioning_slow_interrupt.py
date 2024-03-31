import botocore.session
import boto3
import time

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

def get_skill_details(table_name, skill_name):
    try:
        # Use get_item to fetch the specific item
        response = dynamodb.get_item(
            TableName=table_name, 
            Key={
                "name": {"S": skill_name},  # Assuming name is of type String (S)
            }
        )

        # Extract the item from the response
        item = response.get('Item')

        if item:
            # Convert DynamoDB item to a more readable format
            readable_item = {
                "name": item["name"]["S"],
                "price": item["price"]["N"],
                "is_available": item["is_available"]["S"],
                "version": item["version"]["N"]
            }
            return readable_item
        else:
            print(f"Skill '{skill_name}' not found.")
            return None
    except Exception as e:
        print(f"Failed to retrieve item: {str(e)}")
        return None
    
skill_table = "game-skill-version-001"
skill_name = "potion making"
skill_details = get_skill_details(skill_table, skill_name)
print('skill_details: ', skill_details)

version_expected = int(skill_details["version"])
version_incremented = version_expected + 1

price_new = 888

params = {
    'TableName': skill_table,
    'Key': {
        "name": {'S': skill_details["name"]}
    },
    'UpdateExpression': "SET price = :price, version = :new_version",
    'ConditionExpression': "version = :expected_version",
    'ExpressionAttributeValues': {
        ':price': {'N': str(price_new)},
        ':new_version': {'N': str(version_incremented)},
        ':expected_version': {'N': str(version_expected)},
    }
}

try:   
    response = dynamodb.update_item(**params)
    print(f"Update successful for item ({skill_details['name']})")
except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(f"Condition check failed: Version mismatch. Abort update on item ({skill_details["name"]}")
    else:
        raise
