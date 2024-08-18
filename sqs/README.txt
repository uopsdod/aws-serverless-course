
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
 - update code: "sqs_lambda_程式碼.txt"
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
  - "sqs_lambda_queue_sample_message.txt"

===== 建立高流量情境 ===== 

# 建立 IAM Role for EC2 
 - use case: EC2 
 - policy: AmazonSQSFullAccess
 - name: "role-for-sqs-ec2"

# 建立 VPC 
 - click 'VPC and more'
 - name: "vpc-for-sqs"
 - create 

# 建立 Security Group 
 - name: "mysg-for-sqs-ec2"
 - description: "mysg-for-sqs-ec2"
 - vpc: "vpc-for-sqs"
 - inbound rule: 
  - type: SSH 
  - source: all 
 - inbound rule: 
  - port: 8080 
  - source: all 

# 建立 EC2 
 - Go to EC2 > instances 
 - name: "ec2-for-sqs"
 - ami: Amazon Linux 2023 AMI 
 - no key pair 
 - vpc: "vpc-for-sqs"
  - pick public subnet 
  - enable public ip 
 - security group: "mysg-for-sqs-ec2"
 - click Advanced details > IAM instance profile: "role-for-sqs-ec2"
 - click Launch 

# 建立前端專案 
 - Enter EC2 instance 
 - execute "sqs_lambda_前端專案_安裝指令包.txt"

# 開啟前端頁面 
 - copy EC2 dns name 
 - example: http://ec2-3-140-238-31.us-east-2.compute.amazonaws.com:8080/
 - click 'sqs ad lambda'
 - replcae backend URL (ex: http://ec2-3-140-238-31.us-east-2.compute.amazonaws.com:8080)
 - replace sqs queue url (ex: https://sqs.us-east-2.amazonaws.com/344458213649/sqs-for-lambda)
 - send message batch: 5

# 暫停 SQS Trigger in Lambda 

# 回到前端頁面 
 - click 'Send Message to SQS' 
 - click 'Track SQS Message Count' 
 - send message batch: 45

# 啟動 SQS Trigger in Lambda 

# 回到前端頁面 
 - observe 
 - send message batch: 50 
 - observe 
 - send message batch: 1000
 - observe 
 - send message batch: 1000

# 資源清理 
EC2 instance 
Lambda function 
SQS queue 


