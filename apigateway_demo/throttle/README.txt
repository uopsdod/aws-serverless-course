===== API Gateway 設定 ===== 

# 啟用 Throttling
 - go to Stages 
 - click 'prod' stage
 - Edit it 
 - Enable Throttling
  - limit: 1
  - burst: 1  

# 模擬大量請求 
 - enter ec2 
 - execute the commands 
API_HOSTNAME=https://qdfw4ssbx5.execute-api.us-east-2.amazonaws.com
curl ${API_HOSTNAME}/prod/users/katty
while sleep 0.005; do curl -s ${API_HOSTNAME}/prod/users/katty; echo ""; done
