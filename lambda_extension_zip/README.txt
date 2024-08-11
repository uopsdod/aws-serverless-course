# 回到 EC2 Terminal 

# 進入本單元專案目錄
cd ~/aws-serverless-course/lambda_extension_zip/

# 設定環境參數
AWS_ACCOUNT=659104334423
LAYER_NAME="lambda_library_only"
LAYER_ZIP_FILE="lambda_library_only.zip"
FUNCTION_NAME="lambda_function_only"
HANDLER_NAME="handler"
FUNCTION_ZIP_FILE="lambda_function_only.zip"
LAMBDA_FUNCTION_NAME="simple_function_with_layer_with_extension"

# 打包程式碼
rm $FUNCTION_ZIP_FILE
zip $FUNCTION_ZIP_FILE ${FUNCTION_NAME}.py
ls -lh

# 安裝第三方套件
# Layer paths for python: https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html
python -m venv venv
source venv/bin/activate
pip install requests --target ./python
ls ./python

# 打包第三方套件
# Layer paths for python: https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html
rm -f $LAYER_ZIP_FILE
zip -r $LAYER_ZIP_FILE ./python
ls -lh

# 建立 Lambda Layer 
aws lambda publish-layer-version \
    --layer-name $LAYER_NAME \
    --zip-file fileb://$LAYER_ZIP_FILE
LAYER_VERSION_ARN=XXXXX

# 建立 Lambda Function
aws lambda create-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --runtime python3.12 \
    --zip-file fileb://$FUNCTION_ZIP_FILE \
    --handler $FUNCTION_NAME.$HANDLER_NAME \
    --role arn:aws:iam::${AWS_ACCOUNT}:role/serverless-lambda-role \
    --layers ${LAYER_VERSION_ARN}

# 更新 Lambda Function 使用 Layer
aws lambda update-function-configuration \
    --function-name $LAMBDA_FUNCTION_NAME \
    --layers ${LAYER_VERSION_ARN}

# 測試 Lambda (Console)
 - 點擊 Test - 預期回應: OK

---
# 回到 EC2 Terminal 

# 安裝 Extension 所需套件
cd python-example-extension
chmod +x extension.py
pip3 install -r requirements.txt -t .
cd ..

# 打包 extension.zip
chmod +x extensions/python-example-extension
zip -r extension.zip .

# 建立 Lambda Extension Layer 
aws lambda publish-layer-version \
 --layer-name "python-example-extension" \
 --zip-file  "fileb://extension.zip"
LAYER_VERSION_EXTENSION_ARN=XXXXX

# 使用 Lambda Extension Layer
aws lambda update-function-configuration \
    --function-name $LAMBDA_FUNCTION_NAME \
    --layers $LAYER_VERSION_ARN $LAYER_VERSION_EXTENSION_ARN

# 測試 Lambda (Console)
 - 點擊 Test - 預期回應: OK
 - CloudWatch Logs: "[python-example-extension]"

-----
# Reference - Example Extension in Python
- https://github.com/aws-samples/aws-lambda-extensions/tree/main/python-example-extension
