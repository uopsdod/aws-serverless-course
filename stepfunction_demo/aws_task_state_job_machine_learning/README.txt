
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/aws_task_state_job_machine_learning

# 建立 S3 bucket
 - name: "sagemaker-model-data-iqjdavibsdavsdfvgb"

# 上傳訓練與測試資料 
 - create prefix: "csv"
 - 解說 train.csv
 - 上傳 train.csv & test.csv

# 建立 IAM Role
 - use case: SageMaker 
 - name: "train-model-endpoint-predict-role"
 - policy: AmazonSageMakerFullAccess (added by default), AmazonS3FullAccess 

# 啟動 SageMaker Notebook 
 - instance name: "train-model-endpoint-predict-notebook"
 - instance type: "ml.t3.medium"
 - role: "train-model-endpoint-predict-role"

# 上傳 ipynb 檔案
 - file: "xgboost-001.ipynb"
 - type: "conda_python3"
 - (wait for 5 min ...)
 - click 'Open Jupyter'

# 執行 ipynb 
 - update S3 bucket arn 
 - update iam role 

====
[use step function]

# 建立 S3 bucket
 - name: "sagemaker-model-data-002-wefwfarf"

# 上傳訓練與測試資料 
 - create prefix: "csv"
 - 解說 train.csv
 - 上傳 train.csv & test.csv

# 建立 IAM Role for Step Function 
 - use case: Step Function 
 - name: "train-model-endpoint-predict-role-for-step"
 - policy: AWSLambdaRole (added by default), CloudWatchFullAccessV2, CloudWatcheventsFullAccess, AmazonSageMakerFullAccess 

# 建立 IAM Role for SageMaker
 - use case: SageMaker 
 - name: "train-model-endpoint-predict-role-for-sagemaker"
 - policy: AmazonSageMakerFullAccess (added by default), AmazonS3FullAccess 

# 建立 Lambda Role 
 - policy: AmazonSageMakerFullAccess, CloudWatchFullAccessV2
 - name: "predict-role-for-lambda"

# 建立 step function 
 1. SageMaker - CreatingTrainingJob
  - name: "Train model (XGBoost)"
  - API parameters: "api_create_training_job"
  - click "wait for the task to complete" 
 2. SageMaker - CreateModel 
  - API parameters: "api_create_model"
 3. SageMaker - CreateEndpointConfig
  - API parameters: "api_create_endpoint_config"
 4. SageMaker - CreateEndpoint
  - API parameters: "api_create_endpoint"
 5. Config >> update IAM Role 

# 執行 state machine  
 - (wait for it to create?)
=====
{
    "S3BucketName": "sagemaker-model-data-002-awfsdvadfbg",
    "SageMakerIamRoleArn": "arn:aws:iam::659104334423:role/train-model-endpoint-predict-role-for-sagemaker"
}
=====

# 建立 lambda function
 - name: "predict-lambda-001"
 - runtime: python 
 - role: "predict-role-for-lambda"
 - code: "predict_lambda.py"
 - click 'Deploy'

# 測試 lambda function 01
 - file: "predict_lambda_input_01.txt"
 - change endpoint name 

=====
{
  "endpoint_name": "XXXXX",
  "input_data": "98,25"
}
=====

# 測試 lambda function 02
 - file: "predict_lambda_input_02.txt"
 - change endpoint name 

=====
{
  "endpoint_name": "XXXXX",
  "input_data": "55,95"
}
=====

# 資源清理
 - Sagemaker Model / EndpointConfig / Endpoint 
 - Step Function State Machine 
 - Lambda Function 
 - S3 Bucket 
 - IAM Roles 

===== 








# 查看 Java 版本
java --version

# 下載 mvn 
sudo yum install -y maven
mvn --version

# 下載專案
git clone https://github.com/uopsdod/aws-serverless-course.git
cd aws-serverless-course/lambda_snapstart_hook

# 查看程式碼 
 - pom.xml: "crac" dependency 
 - file: "FunctionHandler.java"

# 建立 Jar 部署檔案 
mvn clean package
ls -lh target/ | grep "jar"
JAR_PATH="target/function-sample-aws-0.0.1-SNAPSHOT-aws.jar"

# 建立 S3 bucket 
S3_BUCKET="lambda-snapstart-hook-fvpoijwreuhoiewurf"
aws s3 mb "s3://${S3_BUCKET}"

# 上傳 Jar 檔案到 S3 bucket 
aws s3 cp $JAR_PATH "s3://${S3_BUCKET}/${JAR_PATH}" 

# 複製 S3 Jar URL 
- example: "https://lambda-snapstart-oinpjniokiuhiu.s3.us-east-2.amazonaws.com/target/function-sample-aws-0.0.1-SNAPSHOT-aws.jar"

# 建立 Lambda Function 
 - name: "function-snapstart-hook-002"
 - runtime: Java 

# 更新 Lambda Handler Code 
 - S3 Jar URL

# 更新 Lambda Handler 設定 
 - handler: "example.FunctionHandler::handleRequest"

# 啟用 SnapStart + 更新 Timeout 
 - Configuration > General configuration > Edit > SnapStart: PublishedVersions
 - Configuration > General configuration > Edit > Timeout: 5 min 

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
 - 2nd: 查看 UUID
  - 再執行一次 Test, 查看 UUID
 - 3rd: 前往 CloudWatch Log, 去看到 "checkpoint hook" > 再看一次 "afterRestore hook"

# 資源清理 
 - Lambda Function 
 - Step Function State Machine 
 - SageMaker Endpoints 
 - SageMaker Endpoints Config 
 - SageMaker Endpoints Models 
 - IAM Role * 2
 - S3 Bucket
