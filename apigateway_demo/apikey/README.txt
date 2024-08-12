
# 建立 Usage Plan 
 - name: "usage-plan-user-profile"
 - throttling: 1, 1 
 - quota: 5 Per day

# 連結 API Key 到 API Stage 

# 建立 API Key 
 - name: "apikey-user-profile-001"
 - click 'create'
 - go back to API Keys List 

# 連結 API Key 到 Usage Plan 
 - click 'Add to usage plan' 

# 設定 API API Key 來源種類 
 - go to API 
 - go to API settings 
 - click Edit 
 - modify/confirm API key source uses 'Header'   
 
# 設定 API Method 使用 API Key 
 - go to api
 - go to Resources 
 - click 'GET' method 
 - click 'Edit' 
 - enable API key required 
 - click 'Deploy'

# 測試

curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "authorizationToken: allow"
 - expect: 403 Forbidden result 

API_KEY=vb4ksjox1u8dkeRTpykkL4QSjsZE40yD2P5VGXMz
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
curl https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com/prod/users/katty -H "x-api-key: ${API_KEY}" -H "authorizationToken: allow" 
 - expect: Limit Exceeded

