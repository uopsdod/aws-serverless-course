import json

def lambda_handler(event, context):
    print("event:", event)

    # Retrieve the path parameters
    path_parameters = event.get('pathParameters', {})
    user_name = path_parameters.get("name")    
    print("path_parameters: ", path_parameters)
    print("user_name: ", user_name)
    
    profile = get_profile(user_name)
    print("profile: ", profile)
    
    # Optional: Return the values in the response
    return {
        'statusCode': 200,
        'body': json.dumps(profile)
    }

def get_profile(user_name):
    # simulating look up 
    if user_name == "katty":
        return {
            'name': user_name,
            'education': 'college',
            'age': 23
        }

    return {}

# For testing purposes, you can manually invoke this handler function
# by passing in a mock event object similar to one provided by API Gateway:
if __name__ == "__main__":
    # Sample event dictionary mimicking API Gateway input
    mock_event = {
        "resource": "/users/{name}/profile",
        "path": "/users/katty/profile",
        "httpMethod": "GET",
        "queryStringParameters": {
            "education": "college",
            "age": "23"
        },
        "pathParameters": {
            "name": "katty"
        },
        "body": "{\"key1\": \"value1\", \"key2\": \"value2\"}"
    }
    
    # Call the handler with a mock event and a placeholder context
    response = lambda_handler(mock_event, None)
    print("Lambda Response:", response)
