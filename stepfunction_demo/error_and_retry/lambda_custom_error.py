import json
import time
import random

def lambda_handler(event, context):
    print('context: ', context)
    print('event: ', event)

    # simulating network connection 
    network_status = is_network_good()
    if network_status:
        time.sleep(1)
    else: 
        # Raising a custom exception if the network is not good
        raise MyNetworkError("Network connection is not good")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

def is_network_good():
    if random.random() > (1/2):
        return True
    else:
        return False

# Define a custom exception
class MyNetworkError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)