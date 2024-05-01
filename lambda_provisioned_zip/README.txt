===== AWS Lambda Provisioned Concurrency ===== 

# 提升 Provisioned Concurrency Quota 

# 確認 Provisioned Concurrency Quota 

# 建立 Lambda 
- name: lambda_function_with_db
- runtime: python3.12
- code: lambda_function_with_db.py

# 設定 handler 
- lambda_function_with_db.lambda_handler 

# 設定 Timeout to 5 min 
- Configuration > General > Timeout

# 建立 version 

# 建立 alias 

# 測試 Lambda (Console)
- 切換到 alias 
- 點擊 Test: 等待 Initialization 
- 點擊 Test: 馬上取得回應 

# 測試 Lambda (Console)
- 設定秒數為 30 秒 
- click 'Deploy' 重新部署 
- 建立 new version 
- 建立 new alias 
- 切換到 alias 
- 點擊 Test: 發現 Timeout (> 10 seconds)

# 設定 Provisioned Concurrency
- 切換到 alias 
- Configuration > Concurrency > Provisioned concurrency configurations > 'Add'
 - 新增 1 個
- 等待部署

# 測試 1st Lambda (Console)
- 切換到 alias 
- 點擊 Test: 等待 Initialization 
- 點擊 Test: 馬上取得回應 

# 測試 2nd Lambda (Console)
- 開啟第二個平行視窗 
- 切換到 alias 
- 點擊 1st Test: 馬上取得回應
- 點擊 2nd Test: 等待 Initialization 
- 點擊 2nd Test: 馬上取得回應 

===== Reference 

# 進入本單元專案目錄
cd ~/aws-serverless-course/lambda_provisioned_zip/
ls

# 設定環境參數
AWS_ACCOUNT=659104334423
FUNCTION_NAME="lambda_function_with_db"
HANDLER_NAME="lambda_handler"
ZIP_FILE="lambda_function_with_db.zip"
LAMBDA_FUNCTION_NAME="lambda_function_with_db"

# 打包程式碼
rm $ZIP_FILE
zip $ZIP_FILE ${FUNCTION_NAME}.py
ls -lh

