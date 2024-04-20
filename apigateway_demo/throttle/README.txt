===== EC2 Linux 共用環境 =====
# 建立 VPC 
- select "VPC and more"
- name: "vpc-api-001"

# 建立 IAM Role for EC2
- name: "api-ec2-role-001"
- policy: "AdministratorAccess"

# 建立 EC2 Instance 
- name: "api-ec2-001"
- no key pair 
- vpc: "vpc-api-001"
- subnet: pick public ones
- enable public ip 
- click Advanced setting
 - pick role "api-ec2-role-001"

===== API Gateway 設定 ===== 

# 啟用 Throttling
 - go to Stages 
 - click 'prod' stage
 - Edit it 
 - Enable Throttling
  - limit: 1
  - burst: 1  

# 模擬大量請求 
 - enter ec2 
 - execute the commands 
api_hostname=https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com
curl ${api_hostname}/prod/users/katty
while sleep 0.005; do curl -s ${api_hostname}/prod/users/katty; echo ""; done

# create iam role for api gateway 
 - use case: API Gateway 
 - policy: AmazonAPIGatewayPushToCloudWatchLogs
 - role name: "api-role-for-cloudwatch"

# set api gateway Setting 
 - go to api gateway 
 - click 'Settings' 
 - click 'Edit' of Logging 
 - pick: "api-role-for-cloudwatch"

# 啟用 Logging and Metrics 
 - go to Stages 
 - click 'prod' stage
 - Edit logs and tracing 
  - select 'Errors and Info logs' 
  - click 'Detailed metrics' 

# 檢查 API Gateway Logs 
 - example log group name: "API-Gateway-Execution-Logs_qdfw4ssbx5/prod"

# 建立 CloudWatch log group
 - name: "access-log-group-for-api-lambda-profile"
 - get arn without "*": arn:aws:logs:us-east-2:659104334423:log-group:log-group-for-api-lambda-profile
 - log format: 
  - "$context.status " 
  - response status: $context.requestId $context.httpMethod $context.resourcePath $context.protocol" 

# 啟用 Access Logging 
 - context info: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference 
 - paste this to capture access logs: 
{ "requestId":"$context.requestId", "extendedRequestId":"$context.extendedRequestId", "requestTime":"$context.requestTime", "protocol":"$context.protocol", "stage:$context.stage", "resourcePath":"$context.resourcePath", "httpMethod":"$context.httpMethod", "status":"$context.status",  "errorMessage:$context.error.message", "errorResponseType:$context.error.responseType" }

# 檢查 CloudWatch log group 
 - log group name: "access-log-group-for-api-lambda-profile"
 - check "429" access logs 





