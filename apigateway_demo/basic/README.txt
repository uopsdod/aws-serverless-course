# 建立 lambda function 
 - name: "lambda-for-apigateway-001"
 - runtime: python 3.12

# 部署 lambda function 
 - code: https://github.com/uopsdod/aws-serverless-course/blob/main/apigateway_demo/basic/lambda_userprofile.py
 - input: https://github.com/uopsdod/aws-serverless-course/blob/main/apigateway_demo/basic/lambda_userprofile_event.json
 - click 'Deploy'

# 建立 api gateway 
 - api type: REST API 
 - name: "api-lambda-profile-001"
 - api endpoint type: regional 

# 建立 resource 
 - resource name: users
  - enable CORS 
 - resource name: {name}
  - enable CORS 

# 建立 method
 - method type: GET
 - Integration type: Lambda 
 - enable 'Lambda proxy Integration'
 - select lambda function 
 - click 'Create method'
 - click 'Deploy API'
  - click *New Stage*
  - name: "prod"

# Go to Stages 
 - expand prod/users/{name}
 - click 'GET' 
 - copy url (example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/{name})
 - replace the path variable: 
  - example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/sam 
  - example: https://whrxkgjfi8.execute-api.us-east-2.amazonaws.com/prod/users/katty





