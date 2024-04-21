import json
import os  # Import os module to access environment variables

def lambda_handler(event, context):
    print("event: ", event)
    token = event['authorizationToken']
    print("token: ", token)
    print("methodArn: ", event['methodArn'])

    apikey = get_apikey(token)
    
    if token == 'allow':
        print('authorized')
        response = generatePolicy('user', 'Allow', event['methodArn'], apikey)
    elif token == 'deny':
        print('unauthorized')
        response = generatePolicy('user', 'Deny', event['methodArn'], apikey)
    elif token == 'unauthorized':
        print('unauthorized')
        raise Exception('Unauthorized')  # Return a 401 Unauthorized response
    
    try:
        return json.loads(response)
    except BaseException:
        print('unauthorized')
        return 'unauthorized'  # Return a 500 error

def get_apikey(token):
    # Use the environment variable if token is 'allow'
    if token == 'allow':
        return os.getenv('API_KEY', '')  # Return empty string if API_KEY is not set
    return ""

def generatePolicy(principalId, effect, resource, apikey):
    authResponse = {}
    authResponse['principalId'] = principalId
    if effect and resource:
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'] = [statementOne]
        authResponse['policyDocument'] = policyDocument
    authResponse['context'] = {
        "stringKey": "stringval",
        "numberKey": 123,
        "booleanKey": True
    }
    if apikey:
        authResponse['usageIdentifierKey'] = apikey
    authResponse_JSON = json.dumps(authResponse)
    return authResponse_JSON
