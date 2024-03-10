===== AWS Lambda 部署模式快速上手：ZIP 檔案 ===== 

# 建立基礎資源 - IAM Role for EC2
- service: EC2 
- policy: AdministratorAccess
- name: "serverless-admin-role"

# 建立基礎資源 - IAM Role for Lambda
- service: Lambda
- policy: AWSLambdaBasicExecutionRole
- name: "serverless-lambda-role"

# 建立基礎資源 - VPC
- click 'VPC and more'
- name: "serverless-vpc"

# 建立基礎資源 - EC2
- name: "serverless-ec2-demo"
- select no key pair
- select VPC
 - select public subnet
 - enable public ip 
- expand 'Advanced details'
 - select iam role "serverless-admin-role"

# 進入 EC2 

# 安裝套件 - git
sudo yum install -y git 

# 安裝套件 - docker 
sudo yum install docker -y

# 設定環境參數
AWS_ACCOUNT=659104334423
FUNCTION_NAME="lambda_simple_function"
HANDLER_NAME="handler"
ZIP_FILE="lambda_simple_function.zip"

# 打包程式碼
rm $ZIP_FILE
zip $ZIP_FILE lambda_simple_function.py
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
 - note: 當部署包 < 3 MB，可直接看到/編輯程式碼
 - 點擊 Test: 查看回應 
