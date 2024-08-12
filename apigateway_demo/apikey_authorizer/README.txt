# 設定 API API Key 來源種類 
 - go to API 
 - go to API settings 
 - click Edit 
 - modify API key source to Authorizer  
 - go to Resources
 - click 'Deploy' 

# 建立 API Key 
 - name: "apikey-user-profile-002"
 - click 'Save'

# 連結 API Key 到 Usage Plan 
 - click 'Add to usage plan' 

# 更新 Lambda Authorizer 
 - code: https://github.com/uopsdod/aws-serverless-course/blob/main/apigateway_demo/apikey/lambda_authorizer_apikey.py
 - click 'Deploy' 
 - go to Configure 
 - add environment variable: 
  - key: API_KEY
  - val: XXXXX 

# 測試 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
 - expect: Limit Exceeded









