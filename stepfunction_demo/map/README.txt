
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/map

# 建立 S3 Bucket 
 - name: "step-function-map-gjcoidjvosid"
 - prefix: "images"
 - upload 10 images: "pangolin_XXX.png"

# 建立 IAM Role 
 - use case: Lambda 
 - policy: AmazonS3FullAccess, CloudWatchFullAccessV2 
 - name: "role-image-resizer-used-in-map" 

# 建立 Lambda 
 - name: "lambda-image-resizer-used-in-map"
 - runtime: python 
 - role: "role-image-resizer-used-in-map" 

# 更新程式碼
 - code: "lambda_image_resizer_used-in-map.py" 
  - https://github.com/uopsdod/aws-serverless-course/blob/main/stepfunction_demo/map/lambda_image_resizer_used-in-map.py 

# 新增 Layer for Pillow 套件  
 - Specify ARN: "arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p312-Pillow:2"
 - source: https://github.com/keithrozario/Klayers/tree/master/deployments/python3.12
  - Pillow example: https://api.klayers.cloud/api/v2/p3.12/layers/latest/us-east-1/html 

# 建立 Step Function State Machine 
Create Map State 
 - name: "Parallel Image Resizers"
 - Processing Mode: "Distributed"
 - Item Source: S3 
 - S3 item source: s3 object list 
 - S3 bucket: from state input 
 - Bucket Name: "$.MyBucketName"
 - Prefix: "$.MyObjectPrefix"
 - expand 'Additional Information'
  - click 'Modify items with ItemSelector'
=====
{
  "bucket_name.$": "$.MyBucketName",
  "object_key.$": "$$.Map.Item.Value.Key",
  "image_size_target.$": "$.MyImageSizeTarget"
}
===== 
 - Runtime settings 
  - concurency limit: 1000
 - Child workflow execution tyep: Express

Create Lambda State inside Map State 
 - name: "Image Resizer"
 - function name: "lambda-image-resizer-used-in-map"
 - Payload: state input 

# 執行 state machine 
=====
{
  "MyBucketName": "step-function-map-sodjavoijvfgb",
  "MyObjectPrefix": "images",
  "MyImageSizeTarget": 100
}
=====
 - click 'Map Run'
  - note: see the status of all execution
  - note: click one of them to see execution input/ouput  
 - check S3 bucket 
  - check "resized/images" folder 

# 上傳 S3 Objects 
 - name: "step-function-map-gjcoidjvosid"
 - prefix: "images"
 - upload 1000 images 

# 執行 state machine 
=====
{
  "MyBucketName": "step-function-map-sodjavoijvfgb",
  "MyObjectPrefix": "images",
  "MyImageSizeTarget": 200
}
=====
 - click 'Map Run'
  - note: see the status of all execution
  - note: click one of them to see execution input/ouput  
 - check S3 bucket 
  - check "resized/images" folder 

# 資源清理 
 - Step Function State Machine 
 - Lambda Function 
 - S3 Bucket 
 - IAM Role 
 