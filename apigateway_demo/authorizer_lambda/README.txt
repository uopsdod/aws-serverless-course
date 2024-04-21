
# 建立 Lambda Function 
 - name: "lambda-authorizer-001"
 - runtime: python 3.12
 - code: _____ 
 - click 'Deploy' 

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
 - name: "lambda-authorizer-001"
 - type: Lambda 
 - role: arn of iam role "role-for-api-lambda-authorizer" 
 - event payload: Token 
 - token source: "authorizationToken" 

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

??? Grant API Gateway permission to invoke your Lambda function. To turn off, update the function's resource policy yourself, or provide an invoke role that API Gateway uses to invoke your function.

