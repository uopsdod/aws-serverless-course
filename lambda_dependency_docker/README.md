# 進入 EC2 Terminal 

# 進入本單元專案目錄
cd ~/aws-serverless-course/lambda_layer_docker

# 啟動 docker
sudo service docker start

# 建立 Docker Image 
docker build -t dependency-function --no-cache .
docker images

# 啟動 Docker 容器
docker run -d --name dependency-function -p 9000:8080 dependency-function:latest
docker container ls 

# 本地測試 
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"key1":"value1"}'

# 關閉 Docker 容器
docker stop dependency-function
docker rm dependency-function

---
# 上傳 Docker Image 到 AWS ECR 
AWS_REGION="us-east-2"
ECR_REPO_NAME="lambda-docker-ecr-repo"
ECR_URL="659104334423.dkr.ecr.us-east-2.amazonaws.com"
ECR_REPO_URL=${ECR_URL}/${ECR_REPO_NAME}
echo $ECR_REPO_URL

# 得到 ECR 上傳權限
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URL

# 上傳本地 Docker Image
docker images
docker tag dependency-function:latest "${ECR_REPO_URL}:latest"
docker images
docker push "${ECR_REPO_URL}:latest"

# 建立 Lambda function 
AWS_ACCOUNT=659104334423
LAMBDA_FUNCTION_NAME="docker-dependency-function"
aws lambda create-function  \
--function-name $LAMBDA_FUNCTION_NAME  \
--role arn:aws:iam::${AWS_ACCOUNT}:role/serverless-lambda-role \
--code ImageUri=$ECR_REPO_URL:latest \
--package-type Image

# 更新 lambda function (optional)
aws lambda update-function-code \
--function-name $LAMBDA_FUNCTION_NAME \
--image-uri $ECR_REPO_URL:latest

# 測試 Lambda (Console)
 - Test - 預測回應: OK 


