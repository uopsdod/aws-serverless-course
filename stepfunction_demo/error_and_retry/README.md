
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/XXXXX 

# 建立 IAM Role 
 - use case: Lambda 
 - policy: CloudWatchFullAccessV2
 - name: "role-network-delay-001" 

# 建立 Lambda 
 - name: "lambda-network-delay-001"
 - runtime: python 
 - role: "role-network-delay-001"

# 設定 Lambda 
 - Configuration > General Configuration > Timeout: 5 min 

# 更新 Lambda 程式碼 
 - code: "lambda_network_delay.py"

# 建立 State Machine 
 - 建立 Lambda 
  - name: "lambda-network-delay-001"
  - lambda: "lambda-network-delay-001"
  - Error Handling - 設定 Timeout: 5s

# 測試 State Machine 
 - 測出一個 OK
 - 測出一個 Timeout 

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

# 測試 State Machine 
 - 查看 Events 
 - 測出一個 OK
 - 測出一個 Timeout 
  - note: 有 retry 發生

# 資源清理 
 - Step Function State Machine 
 - Lambda Function 
 - IAM Role 
 