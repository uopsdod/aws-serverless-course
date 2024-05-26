
# 建立 S3 Bucket 
 - name: "image-resizer-icauhdscoiciauhodsiu"

# 上傳 S3 File 
 - file: "aws_icon.png"

# 建立 IAM Role 
 - use case: Lambda 
 - policy: AmazonS3FullAccess, CloudWatchFullAccessV2 
 - name: "role-image-resizer" 

# 建立 Lambda 
 - name: "lambda-image-resizer"
 - runtime: python 
 - role: "role-image-resizer" 

# 新增 Layer for Pillow 套件  
 - arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p312-Pillow:2
 - source: https://github.com/keithrozario/Klayers/tree/master/deployments/python3.12

# 更新程式碼
 - code: "lambda_image_resizer.py" 

# 建立 State Machine 
 - Add Parallel State 
  - enable ResultPath & Discard output
 - Add Another Parallel State 
  - enable ResultPath & Discard output
 - Add Pass State 1
  - enable Paramters: 
=====
{
  "image_size_target.$": "$.image_size_target_1"
}
=====
  - enable ResultPath; "$.taskoutput" 
 - Add Lambdas
  - pick "lambda-image-resizer"
 - Add Pass State 2
 - Add Pass State 3 

# 測試 State Machine 
Input 
=====
{
  "bucket_name": "image-resizer-icauhdscoiciauhodsiu",
  "object_key": "aws_icon.png",
  "image_size_target_1": 300,
  "image_size_target_2": 500,
  "image_size_target_3": 700
}
====

# 資源清理 
 Lambda Function 
 S3
 IAM Role 
 State Machine  