===== AWS Lambda Provisioned Concurrency ===== 

# 提升 Provisioned Concurrency Quota 
- Service Quota > Lambda > Concurrent executions
 - Requested quota value: 1,000 

# 確認 Provisioned Concurrency Quota 

# 建立 Lambda 
- name: lambda_function_with_db_001
- runtime: python3.12

# 設定 Timeout to 5 min 
- Configuration > General > Timeout

# 更新程式碼 
- code: lambda_function_with_db.py
https://github.com/uopsdod/aws-serverless-course/blob/main/lambda_provisioned_zip/lambda_function_with_db.py

# 測試 Lambda (Console)
- 點擊 Test: 等待 Initialization 
- 點擊 Test: 馬上取得回應 

# 測試 Lambda (Console)
- 設定秒數為 20 秒 
- click 'Deploy' 重新部署 
- 點擊 Test: 發現 Init Timeout (> 10 seconds)

# 建立 Version 
- Actio > Publish new version
- version description: v1 

# 建立 Alias 
- name: a1
- version: v1 

# 設定 Provisioned Concurrency
- 確認目前在 alias a1
- Configuration > Concurrency > Provisioned concurrency configurations > 'Add'
 - 新增 1 個
- 等待部署

# 測試 1st Lambda (Console)
- 確認目前在 alias a1
- 點擊 Test: 馬上取得回應 
 - 不再有 Init Timeout (> 10 seconds)

# 測試 2nd Lambda (Console)
- 開啟第二個平行視窗 
- 確認目前在 alias a1
- 點擊 1st Test: 馬上取得回應
- 點擊 2nd Test: 等待 Initialization 
 - 非 provisioned concurrency 
- 點擊 2nd Test: 馬上取得回應 
