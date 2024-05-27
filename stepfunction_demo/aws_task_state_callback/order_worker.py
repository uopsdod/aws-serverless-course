import json
import boto3
import time

def lambda_handler(event, context):
    print('context: ', context)
    print('event: ', event)
    print('Records: ', event['Records'])
    print('Records[0]: ', event['Records'][0])
    print('body: ', event['Records'][0]['body'])
    
    myBody = json.loads(event['Records'][0]['body'])

    print('orderPrice: ', myBody['orderPrice'])
    print('orderType: ', myBody['orderType'])
    print('myTaskToken: ', myBody['myTaskToken'])
    
    # Simluating Working On Order ... 
    time.sleep(1)

    # Extract the task token
    task_token = myBody['myTaskToken']

    # Create a Step Functions client
    client = boto3.client('stepfunctions')

    # Send the task success signal to the state machine
    response = client.send_task_success(
        taskToken=task_token,
        output=json.dumps({
            'orderPrice': myBody['orderPrice'],
            'orderType': myBody['orderType']
        })
    )

    print('Step Functions response: ', response)

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }