
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
 - Click Configuration > General Configuration > Timeout: 5 min
 - update code: 
