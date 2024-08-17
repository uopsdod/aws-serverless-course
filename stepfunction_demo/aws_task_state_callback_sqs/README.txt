
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/aws_task_state_callback_sqs 

# 建立 SQS 
 - type: "standard"
 - name: "order-queue-001"

# 建立 step function 
 - add SQS.sendMessage
  - name: "send order"
  - sqs: "order-queue-001"
  - enable callback 
  - 修改 Message 
=====
{
  "orderPrice.$": "$.orderPrice",
  "orderType.$": "$.orderType",
  "myTaskToken.$": "$$.Task.Token"
}
=====

# 執行 state machine 
=====
{
  "orderPrice": 999,
  "orderType": "furniture"
}
===== 

# 建立 IAM Role 
 - use case: Lambda 
 - policy: CloudWatchFullAccessV2, AmazonSQSFullAccess, AWSStepFunctionsFullAccess
 - name: "role-order-worker-001" 

# 建立 Lambda 
 - name: "lambda-order-worker-001"
 - runtime: python 
 - role: "role-order-worker-001"
 - Go to Configuration > General Configuration > Timeout: 5 min 

# 更新 Lambda 程式碼
 - code: "order_worker.py" 
   - https://github.com/uopsdod/aws-serverless-course/blob/main/stepfunction_demo/aws_task_state_callback_sqs/order_worker.py

# 建立 Lambda Trigger 
 - sqs: "order-queue-001"

# 查看 State Machine  

# 查看 Lambda Logs 

# 再次執行 state machine 
=====
{
  "orderPrice": 888,
  "orderType": "grocery"
}
===== 

# 查看 State Machine  

# 資源清理 
 - Step Function State Machine 
 - Lambda Function 
 - IAM Role 
 - SQS Queue  
