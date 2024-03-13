===== AWS Lambda 部署模式快速上手：ZIP 檔案 ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/lambda_simple_zip/
ls

# 設定環境參數
AWS_ACCOUNT=659104334423
FUNCTION_NAME="lambda_function_only"
HANDLER_NAME="handler"
ZIP_FILE="lambda_function_only.zip"
LAMBDA_FUNCTION_NAME="simple_function"

# 打包程式碼
rm $ZIP_FILE
zip $ZIP_FILE ${FUNCTION_NAME}.py
ls -lh

# 建立 Lambda 
aws lambda create-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --runtime python3.12 \
    --zip-file fileb://$ZIP_FILE \
    --handler $FUNCTION_NAME.$HANDLER_NAME \
    --role arn:aws:iam::${AWS_ACCOUNT}:role/serverless-lambda-role

# 更新 Lambda (optional)
aws lambda update-function-code \
    --function-name $LAMBDA_FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

# 測試 Lambda (Console)
 - note: 當部署包 < 3 MB，可直接看到/編輯程式碼
 - 點擊 Test: 查看回應 
