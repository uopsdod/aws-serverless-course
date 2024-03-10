import json
import sys
import requests

def handler(event, context):
    print("search_path: ", sys.path)
    response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_location = response.json()  # Parse the JSON response

    return {
        'statusCode': 200,
        'body': json.dumps(iss_location)
    }