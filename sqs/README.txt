
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/sqs

# AWS Region
 - Virginia (us-east-1)

# 建立 IAM Role for Lambda 
 - use case: lambda 
 - policy: AWSLambdaBasicExecutionRole, AmazonSQSFullAccess
 - name: "role-for-sqs-lambda"

# 建立 Lambda Function 
 - name: "sqs-lambda"
 - runtime: NodeJS 
 - role: "role-for-sqs-lambda"
 - Click Configuration > General Configuration > Timeout: 20 seconds 
 - update code: https://github.com/uopsdod/aws-serverless-course/blob/main/sqs/sqs_lambda_%E7%A8%8B%E5%BC%8F%E7%A2%BC.js
 - Deploy 

# 建立 SQS Queue 
 - type: Standard 
 - name: "sqs-for-lambda"
 - visibility timeout: 30 seconds 

# 連結 Lambda + SQS 
 - click Add trigger 
  - sqs name: "sqs-for-lambda"
  - batch size: 1 
  - batch window: 0 

# 寄出 SQS Message 
 - go to SQS queue 
 - click 'Send and receive messages' 
 - enter message body 
=====
{
  "process_time_ms": 1001
}
===== 


