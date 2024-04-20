
# add cloudwatch role to your account for api gateway 
 - use case: API Gateway 
 - policy: AmazonAPIGatewayPushToCloudWatchLogs
- role name: api-role-for-cloudwatch

# create a lambda function 
 - name: "lambda-for-apigateway-001"
 - runtime: python 3.12

# deploy lambda function 


# create a api gateway 
 - api type: REST API 
 - name: "api-lambda-profile-002"
 - api endpoint type: regional 

# create a resource 
 - resource name: users
 - resource name: {name}

# create a method
 - method type: ANY
 - Integration type: Lambda 
 - enable 'Lambda proxy Integration'
 - select lambda function 
 - click 'Deploy API'
  - click *New Stage*
  - name: "prod"

# Go to Stages 
 - expand prod/users/{name}
 - copy url (example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/{name})
 - replace the path variable: 
  - example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/katty
  - example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/sam 



