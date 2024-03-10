# 回到 EC2 Terminal 

# 設定環境參數
AWS_ACCOUNT=659104334423
LAYER_NAME="lambda_library_only"
LAYER_ZIP_FILE="lambda_library_only.zip"
FUNCTION_NAME="lambda_only_function"
HANDLER_NAME="handler"
FUNCTION_ZIP_FILE="lambda_only_function.zip"

# 打包程式碼
rm $FUNCTION_ZIP_FILE
zip $FUNCTION_ZIP_FILE ${FUNCTION_NAME}.py
ls -lh

# 建立 Lambda 
aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --runtime python3.12 \
    --zip-file fileb://$FUNCTION_ZIP_FILE \
    --handler $FUNCTION_NAME.$HANDLER_NAME \
    --role arn:aws:iam::${AWS_ACCOUNT}:role/serverless-lambda-role

# 測試 Lambda (Console)
 - 點擊 Test - 預期回應: "Unable to import module 'lambda_function_only': No module named 'requests'"

--- 

# 安裝第三方套件
# - python 套件需要在 python/ 目錄底下 
python -m venv venv
source venv/bin/activate
pip install requests --target ./python
ls ./python

# 打包第三方套件
# - python 套件需要在 python/ 目錄底下 
rm -f $LAYER_ZIP_FILE
zip -r $LAYER_ZIP_FILE ./python
ls -lh

# 建立 Lambda Layer 
aws lambda publish-layer-version \
    --layer-name $LAYER_NAME \
    --zip-file fileb://$LAYER_ZIP_FILE
LAYER_VERSION_ARN=XXXXX

# 更新 Lambda Function 使用 Layer
aws lambda update-function-configuration \
    --function-name $FUNCTION_NAME \
    --layers ${LAYER_VERSION_ARN}

# 測試 Lambda (Console)
 - 點擊 Test - 預期回應: OK

