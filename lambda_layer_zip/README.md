# 回到 EC2 Terminal 

# 設定環境參數
AWS_ACCOUNT=659104334423
LAYER_NAME="lambda_layer_python_library"
LAYER_ZIP_FILE="lambda_layer_python_library.zip"
FUNCTION_NAME="lambda_function_only"
HANDLER_NAME="handler"
FUNCTION_ZIP_FILE="lambda_function_only.zip"

# 安裝第三方套件
python -m venv venv
source venv/bin/activate
pip install requests
ls venv/lib/python3.9/site-packages/
 - you should see 'requests' folder 

# 打包第三方套件
YOUR_WORK_FOLDER=$(pwd)
echo $YOUR_WORK_FOLDER
cd venv/lib/python3.9/site-packages/
rm -f ${YOUR_WORK_FOLDER}/${LAYER_ZIP_FILE}
zip -r ${YOUR_WORK_FOLDER}/${LAYER_ZIP_FILE} ./
cd ${YOUR_WORK_FOLDER}
ls -lh

# 建立 Lambda Layer 
aws lambda publish-layer-version \
    --layer-name $LAYER_NAME \
    --zip-file fileb://$LAYER_ZIP_FILE

# 打包程式碼
rm $FUNCTION_ZIP_FILE
zip $FUNCTION_ZIP_FILE ${FUNCTION_NAME}.py

# 更新 Lambda
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$FUNCTION_ZIP_FILE

# 測試 Lambda (Console)
 - note: note: 無法直接看到/編輯程式碼了
 - 點擊 Test - 預期回應: OK

---- 

# 回到 EC2 Terminal 

# 模擬大量第三方套件安裝
dd if=/dev/zero of=many_dependencies bs=1M count=500
sudo zip ${ZIP_FILE} many_dependencies
unzip -l ${ZIP_FILE} | awk 'BEGIN {sum=0} {sum += $1} END {print sum / 1024 / 1024 " MB"}'

# 更新 Lambda (optional)
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://$ZIP_FILE

 - 預期回應: "An error occurred (InvalidParameterValueException) when calling the UpdateFunctionCode operation: Unzipped size must be smaller than 262144000 bytes"
