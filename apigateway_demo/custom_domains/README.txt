# 確認 API Resource CORS 已經啟用 (*)
 - otherwise, you'll receive forbidded 403 response in the end in browser
 - howerver, you should be good via command lines. 

# 確認已經擁有 Public Domain 
# 確認已經擁有 Hosted Zone 

# 建立 ACM Certificate 
 - domain: "myapi003.learncodebypicture.com"
 - request public certificate 
 - pick "DNS Validation"
 - click 'Create Record in Route53'

# 建立 A Record 
 - go to Hosted Zone 
 - create A Record from "myapi003.learncodebypicture.com" to your API Gateway API 

# 建立 API Gateway Custom Domain
# 建立 API Mapping 

# 測試 
https://m0g097npi0.execute-api.us-east-1.amazonaws.com/prod/users/katty 
https://myapi003.learncodebypicture.com/users/katty
 - no need to specify stage here 
