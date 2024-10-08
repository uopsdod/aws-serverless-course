
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/aws_task_state

# 建立 S3 Bucket 
 - name: "image-resizer-icauhdscoiciauhodsiu"

# 上傳 S3 File 
 - file: "aws_icon.jpeg"
 - https://github.com/uopsdod/aws-serverless-course/blob/main/stepfunction_demo/aws_icon.jpeg

# 建立 IAM Role 
 - use case: Lambda 
 - policy: AmazonS3FullAccess, CloudWatchFullAccessV2 
 - name: "role-image-resizer" 

# 建立 Lambda 
 - name: "lambda-image-resizer"
 - runtime: python 
 - role: "role-image-resizer" 

# 更新程式碼
 - code: "lambda_image_resizer.py" 
  - https://github.com/uopsdod/aws-serverless-course/blob/main/stepfunction_demo/aws_task_state/lambda_image_resizer.py

# 新增 Layer for Pillow 套件  
 - example: arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p312-Pillow:2
   - make sure to pick the right aws region 
 - source: https://github.com/keithrozario/Klayers/tree/master/deployments/python3.12
   - Pillow example: https://api.klayers.cloud/api/v2/p3.12/layers/latest/us-east-1/html 
 - add a Layer to the lambda function 

# 建立 State Machine 
 - Add Parallel State 
   - Click Output > enable ResultPath & Discard output
 - Add Another Parallel State 
   - Click Output > enable ResultPath & Discard output
 - Add Pass State 1
   - Click Input > enable Parameters 
```
{
  "image_size_target.$": "$.image_size_target_1"
}
```
   - Click Output > enable ResultPath: "$.taskoutput" 
 - Add Pass State 2
   - Click Input > enable Parameters 
```
{
  "image_size_target.$": "$.image_size_target_2"
}
```
   - Click Output > enable ResultPath: "$.taskoutput" 
 - Add Pass State 3
   - Click Input > enable Parameters 
```
{
  "image_size_target.$": "$.image_size_target_3"
}
```
   - Click Output > enable ResultPath: "$.taskoutput" 
 - Add Lambdas
   - name: "image-resizer-001"
   - pick "lambda-image-resizer"
 - Add Lambdas
   - name: "image-resizer-002"
   - pick "lambda-image-resizer"
 - Add Lambdas
   - name: "image-resizer-003"
   - pick "lambda-image-resizer"   

# 測試 State Machine 
Input 
 - replace the bucket_name accordingly
```
{
  "bucket_name": "image-resizer-icauhdscoiciauhodsiu",
  "object_key": "aws_icon.jpeg",
  "image_size_target_1": 300,
  "image_size_target_2": 500,
  "image_size_target_3": 700
}
```

# 檢查 S3 Resized 圖片結果
- Go to S3 Bucket and check

# 查看 Step Function State Machine Input & Output
- Go to Step Function State Machine and check

# 資源清理 
 Lambda Function 
 S3
 IAM Role 
 State Machine  