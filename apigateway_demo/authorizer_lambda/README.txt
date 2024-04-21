
# 建立 Lambda Function 
 - name: "lambda-authorizer-001"
 - runtime: python 3.12
 - code: https://github.com/uopsdod/aws-serverless-course/blob/main/apigateway_demo/authorizer_lambda/lambda_authorizer.py
 - click 'Deploy' 
 - input: https://github.com/uopsdod/aws-serverless-course/blob/main/apigateway_demo/authorizer_lambda/lambda_authorizer_event.json

# 建立 IAM Role 
 - use case: Lambda  
 - policy: AWSLambdaRole 
 - name: "role-for-api-lambda-authorizer"

# 允許 API Gateway 使用 IAM Role
 - edit trusted entity:
==== 
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"Service": "lambda.amazonaws.com"
			},
			"Action": "sts:AssumeRole"
		},
		{
			"Effect": "Allow",
			"Principal": {
				"Service": "apigateway.amazonaws.com"
			},
			"Action": "sts:AssumeRole"
		}
	]
}
==== 

# 建立 Lambda Authorizer 
 - go to api gateway: your API 
 - name: "api-lambda-authorizer-001"
 - type: Lambda 
 - role: arn of iam role "role-for-api-lambda-authorizer" 
 - event payload: Token 
 - token source: "authorizationToken" 
 - disable caching

# 測試 Lambda Authorizer 
 - "allow": expect 200 response with Allow effect 
 - "deny": expect 200 response with Deny effect 
 - "unauthorized": expect 401 response 

# 設定 API Method 使用 Lambda Authorizer 
 - go to Resources
 - click GET method 
 - Edit it 
  - select "lambda-authorizer-001"
 - click 'Deploy' 
  - select 'prod' stage 

# 測試 Lambda Authorizer on API 
 - go to Stages 
 - expand 'prod' 
 - click 'GET' 

curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty
 - expect: 401 Unauthorized
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow" 
 - expect: 200 allow result  
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: deny" 
 - expect: 200 deny result  

