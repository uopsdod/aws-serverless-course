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
        time.sleep(10)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

def is_network_good():
    if random.random() > (1/2):
        return True
    else:
        return False
