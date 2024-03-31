import boto3

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
                "is_available": item["is_available"]["S"]
            }
            return readable_item
        else:
            print(f"Skill '{skill_name}' not found.")
            return None
    except Exception as e:
        print(f"Failed to retrieve item: {str(e)}")
        return None

def get_player_details(table_name, player_name):
    try:
        # Use get_item to fetch the specific item
        response = dynamodb.get_item(
            TableName=table_name, 
            Key={
                "name": {"S": player_name}  # Assuming name is of type String (S)
            }
        )

        # Extract the item from the response
        item = response.get('Item')

        if item:
            # Convert DynamoDB item to a more readable format
            readable_item = {
                "name": item["name"]["S"],
                "money": item["money"]["N"],
                "skills": item["skills"]["SS"]
            }
            return readable_item
        else:
            print(f"Skill '{player_name}' not found.")
            return None
    except Exception as e:
        print(f"Failed to retrieve item: {str(e)}")
        return None

skill_table = "game-skill-001"
skill_name = "lighting power"
skill_details = get_skill_details(skill_table, skill_name)
print('skill_details: ', skill_details)

player_table = "game-player-001"
player_name = "Jane"
player_details = get_player_details(player_table, player_name)
print('player_details: ', player_details)

# Check if the player can buy the skill
if skill_details["is_available"] == "true" and player_details["money"] >= skill_details["price"]:
    try:
        response = dynamodb.transact_write_items(
            TransactItems=[
                {
                    'Update': {
                        'TableName': player_table,
                        'Key': {
                            'name': {'S': player_details["name"]}
                        },
                        'UpdateExpression': 'SET money = money - :price ADD skills :new_skill',
                        'ExpressionAttributeValues': {
                            ':price': {'N': str(skill_details["price"])},
                            ':new_skill': {'SS': [skill_details["name"]]}
                        },
                        'ConditionExpression': 'money >= :price'
                    }
                },
                {
                    'Update': {
                        'TableName': skill_table,
                        'Key': {
                            'name': {'S': skill_details["name"]}
                        },
                        'UpdateExpression': 'SET is_available = :false',
                        'ExpressionAttributeValues': {
                            ':false': {'S': 'false'}
                        },
                        'ConditionExpression': 'attribute_exists(non_exist_field)'  # simulate the failed write_item case 
                    }
                }
            ]
        )
        print("Transaction successful.")
    except Exception as e:
        print("Transaction failed:", e)
else:
    print("Player cannot afford the skill or the skill is not available.")


skill_details = get_skill_details(skill_table, skill_name)
print('skill_details: ', skill_details)

player_details = get_player_details(player_table, player_name)
print('player_details: ', player_details)

