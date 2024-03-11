# 回到 EC2 Terminal 

# 進入本單元專案目錄
cd ~/aws-serverless-course/lambda_dependency_zip/

# 設定環境參數
AWS_ACCOUNT=659104334423
FUNCTION_NAME="lambda_function_only"
HANDLER_NAME="handler"
ZIP_FILE="bundled_function.zip"
LAMBDA_FUNCTION_NAME="bundled_function"

# 打包 Lambda 程式碼
rm -f $ZIP_FILE
zip ${ZIP_FILE} ${FUNCTION_NAME}.py
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
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

# 測試 Lambda (Console)
 - 點擊 Test - 預期回應: expect error: "Unable to import module 'lambda_dependency_function': No module named 'requests'"

---- 

# 回到 EC2 Terminal 

# 安裝第三方套件
# - python 套件需要在 Lambda 根目錄底下
python -m venv venv
source venv/bin/activate
pip install requests
ls venv/lib/python3.9/site-packages/
 - you should see 'requests' folder 

# 打包第三方套件
# - python 套件需要在 Lambda 根目錄底下
YOUR_WORK_FOLDER=$(pwd)
echo $YOUR_WORK_FOLDER
cd venv/lib/python3.9/site-packages/
rm -f ${YOUR_WORK_FOLDER}/${ZIP_FILE}
zip -r ${YOUR_WORK_FOLDER}/${ZIP_FILE} ./
cd ${YOUR_WORK_FOLDER}
ls -lh

# 打包程式碼
zip -g $ZIP_FILE ${FUNCTION_NAME}.py
unzip -l $ZIP_FILE | awk 'BEGIN {sum=0} {sum += $1} END {print sum / 1024 / 1024 " MB"}'
 - 預期大於 3 MB

# 更新 Lambda
aws lambda update-function-code \
    --function-name $LAMBDA_FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

# 測試 Lambda (Console)
 - note: note: 無法直接看到/編輯程式碼了
 - 點擊 Test - 預期回應: OK

---- 

# 回到 EC2 Terminal 

# 模擬大量第三方套件安裝
dd if=/dev/zero of=many_dependencies bs=1M count=500
zip ${ZIP_FILE} many_dependencies
unzip -l ${ZIP_FILE} | awk 'BEGIN {sum=0} {sum += $1} END {print sum / 1024 / 1024 " MB"}'

# 更新 Lambda (optional)
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

 - 預期回應: "An error occurred (InvalidParameterValueException) when calling the UpdateFunctionCode operation: Unzipped size must be smaller than 262144000 bytes"
