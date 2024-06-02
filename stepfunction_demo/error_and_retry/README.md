
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/error_and_retry 

# 建立 IAM Role 
 - use case: Lambda 
 - policy: CloudWatchFullAccessV2
 - name: "role-network-delay-001" 

# 建立 Lambda  
 - name: "lambda-network-delay-001"
 - runtime: python 
 - role: "role-network-delay-001"

# 設定 Lambda 
 - Configuration > General Configuration > Timeout: 5 minutes  

# 更新 Lambda 程式碼 
 - code: "lambda_network_delay.py"
 - click 'Deploy'

# 建立 State Machine 
 - 建立 Lambda Invoke State 
  - name: "Potential Network Delay Call"
  - lambda: "lambda-network-delay-001"
  - Error Handling - 設定 Timeout: 5 seconds 
 - Create

# 測試 State Machine 
 - 測出一個 OK
  - click 'Events'
 - 測出一個 Timeout 
  - click 'Events'
  - expand 'Cause'  

# 更新 State Machine
 - Error Handling 
  - Retry on errors
   - Add New a Retrier: States.Timeout 

# 測試 State Machine 
 - 查看 Events 

# 示範 Custom Error 
# 更新 Lambda 程式碼 
 - code: "lambda_custom_error.py"

# 測試 State Machine 
 - 查看 Events 
 - 測出一個 OK
 - 測出一個 Timeout 
  - note: 沒有 retry 發生

# 更新 State Machine
 - Error Handling 
  - Retry on errors
   - Add New a Retrier: MyNetworkError 
    - press Enter 

# 測試 State Machine 
 - 查看 Events 
 - 測出一個 OK
 - 測出一個 Timeout 
  - note: 有 retry 發生

# 資源清理 
 - Lambda Function 
 - Step Function State Machine 
 - IAM Role 
 