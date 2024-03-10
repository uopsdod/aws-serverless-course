import requests
import json

def handler(event, context):
    response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_location = response.json()  # Parse the JSON response

    return {
        'statusCode': 200,
        'body': json.dumps(iss_location)
    }