import json
import boto3

def lambda_handler(event, context):
    # Invoke the Endpoint for Real-time Predictions
    endpoint_name = event.get("endpoint_name")
    input_data = event.get("input_data")
    runtime_client = boto3.client('sagemaker-runtime')

    # probability score that represents the likelihood of the input belonging to the positive class (in this case, class 1)
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',
        Body=input_data
    )
    
    result = response['Body'].read().decode('utf-8')
    print(f'Probability predicted result: {result}')
    
    threshold = 0.5
    binary_prediction = 1 if float(result) > threshold else 0
    print(f'Binary predicted result: {binary_prediction}')
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({
            'input_data': input_data,
            'prediction': binary_prediction
        })
    }


