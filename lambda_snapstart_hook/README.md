
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/lambda_snapstart_hook

# 開啟 Cloud9 
 - name: "lambda-snapstart"

# 下載專案
cd aws-serverless-course/lambda_snapstart_hook/
git pull 

# 查看程式碼 
 - pom.xml: "crac" dependency 
 - file: "FunctionHandler.java"

# 建立 Jar 部署檔案 
mvn clean package
ls -lh target/ | grep "jar"
JAR_PATH="target/function-sample-aws-0.0.1-SNAPSHOT-aws.jar"

# 建立 S3 bucket 
S3_BUCKET="lambda-snapstart-oinpjniokiuhiu"
aws s3 mb "s3://${S3_BUCKET}"

# 上傳 Jar 檔案到 S3 bucket 
aws s3 cp $JAR_PATH "s3://${S3_BUCKET}/${JAR_PATH}" 

# 複製 S3 Jar URL 
- example: "https://lambda-snapstart-oinpjniokiuhiu.s3.us-east-2.amazonaws.com/target/function-sample-aws-0.0.1-SNAPSHOT-aws.jar"

# 建立 Lambda Function 
 - name: "function-snapstart-hook-001"
 - runtime: Java 

# 更新 Lambda Handler Code 
 - S3 Jar URL

# 更新 Lambda Handler 設定 
 - handler: "example.FunctionHandler::handleRequest"

# 更新 Timeout 
 - 5 min 

# 測試
 - 放上 Input 
=====
{
    "name": "Sam001"
}
===== 
 - 注意執行時間
  - Init Duration: 5s
  - (Handler) Duration: 3s
 - 查看 log 

# 啟用 SnapStart 
 - Configuration > General configuration > Edit > SnapStart: PublishedVersions

# 建立 Version v1 
 - 注意: "Creating version 1 of function ... SnapStart adds a few minutes to the version creation process." 

# 測試 Version v1 
 - 放上 Input 
=====
{
    "name": "Sam001"
}
===== 
- 注意執行時間
 - Init Duration: 0s
 - Restore Duration: 0.6s
 - (Handler) Duration: 3s
- 查看 log 
 - 1st: 先看到 "afterRestore hook"
 - 2nd: 前往 CloudWatch Log, 去看到 "checkpoint hook" > 再看一次 "afterRestore hook"


# 資源清理 
Cloud9 Environment 
Labmda Function 
S3 Bucket 

