# 回到 EC2 Terminal 

# 設定環境參數
AWS_ACCOUNT=659104334423
FUNCTION_NAME="lambda_dependency_function"
HANDLER_NAME="handler"
ZIP_FILE="lambda_dependency_function.zip"

# 打包 Lambda 程式碼
rm $ZIP_FILE
zip ${ZIP_FILE} lambda_dependency_function.py
ls -lh

# 建立 Lambda 
aws lambda create-function \
    --function-name $FUNCTION_NAME \
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
python -m venv venv
source venv/bin/activate
pip install requests
ls venv/lib/python3.12/site-packages/
 - you should see 'requests' folder 

# 打包第三方套件
zip -r $ZIP_FILE ./
ls -lh

# 打包程式碼
sudo zip -g ${ZIP_FILE} ${FUNCTION_FILE}
unzip -l ${ZIP_FILE} | awk 'BEGIN {sum=0} {sum += $1} END {print sum / 1024 / 1024 " MB"}'
 - see the file size is now > 3MB 

# 更新 Lambda (optional)
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

# 測試 Lambda (Console)
 - note: note: 無法直接看到/編輯程式碼了
 - 點擊 Test - 預期回應: OK

---- 

# 回到 EC2 Terminal 

# 模擬大量第三方套件安裝
dd if=/dev/zero of=many_dependencies bs=1M count=250
sudo zip ${ZIP_FILE} many_dependencies
unzip -l ${ZIP_FILE} | awk 'BEGIN {sum=0} {sum += $1} END {print sum / 1024 / 1024 " MB"}'

# 更新 Lambda (optional)
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

# 測試 Lambda (Console)
 - note: note: 無法直接看到/編輯程式碼了
 - 點擊 Test - 預期回應: "Unzipped size must be smaller than 262144000 bytes"
