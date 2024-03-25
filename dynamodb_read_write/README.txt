===== Console 操作 ===== 

# 建立 Table 
table name: game-001
partition key; "hour"
 - type: Number 
sort key: "type"
 - type: String 
table setting: 
 - click Customize setting
 - Capacity mode: On-demand 
 - refresh the whole page afterward 

# 建立 Item 
click Action -> create item 
 [item01]
 - Number:hour: 10
 - String:type: baseball
 - Number:duration: 121
 - String:winner: tommy919
 - String Set:players: "kkdd303", "tommy919", "yoyodi"

click [item01] -> Action -> duplicate item
 [item02]
 - Number:hour: 11
 - String:type: poker
 - Number:duration: 312
 - String:winner: yoyodi
 - String Set:players: "harry", "zebie", "yoyodi"
 - Boolean:is_vip: True 

click [item02] -> Action -> duplicate item
 [item03]
 - Number:hour: 12
 - String:type: tennis
 - Number:duration: 70
 - String:winner: kkdd303
 - String Set:players: "kkdd303", "zebie", "yoyodi"
 - Boolean:is_vip: False

# 更新 Item  
click [item01] -> Action -> Edit item 
 - Boolean:is_vip: False

# 刪除 Item 
click [item03] -> Action -> delete item 

===== Python 程式碼操作 =====

# 安裝第三方套件
# - python 套件需要在 Lambda 根目錄底下
python3 -m venv venv
source venv/bin/activate
pip3 install boto3

# 建立 Table 
python3 dynamodb_01_create_table.py

# 建立測試資料
python3 dynamodb_05_add_items_1000.py
python3 dynamodb_06_add_bulk_items_1000.py 

# Get Item 示範 

# Query 示範 
 - 查看 Read Capacity 用量
 - 限制: 無法查詢 is_vip 欄位 

# Scan 示範 
 - 查看 Read Capacity 用量

 ===== 建立 DAX ===== 

 # 安裝第三方套件
# - python 套件需要在 Lambda 根目錄底下
python3 -m venv venv
source venv/bin/activate
pip3 install boto3
pip3 install amazon-dax-client

# 建立 VPC 
- name: "vpc-dynamodb-001"

# 建立 Security Group
- name: "dynamodb-dax-001"
- description: "dynamodb-dax-001"
- port: 8111
- port: 9111 

# 建立 IAM Role for DAX 
- Service: DynamoDB
 - Use Case: Amazon DynamoDB Accelerator (DAX) - DynamoDB access
- name: "dax-to-dynamodb-role-001"

# 建造 DAX Cluster 
- cluster name: "dax-cluster-demo-001" 
- Node family: t-type family
- subnet Group: "subnet-group-001"
 - pick VPC
  - Subnet 
  - Security Group
- iam role: "dax-to-dynamodb-role-001"
- Parameter Group
 - TTL: Item time-to-live (TTL)
 - TTL: Query time-to-live (TTL)

# 建立 IAM Role for EC2
- name: "dynamodb-dax-ec2-role"

# 建立 EC2 Instance 

# 進入 EC2 Instance 

===== 使用 DAX ===== 

# 查詢到內容
python3 dynamodb_15_query_item_with_dax.py 

# 刪除 Table 
python3 dynamodb_10_delete_table.py

# 收到錯誤
python3 dynamodb_15_query_item_with_dax.py

# 建立 Table 
python3 dynamodb_01_create_table.py 

# 收到空白內容 
python3 dynamodb_15_query_item_with_dax.py

# 建立測試資料
python3 dynamodb_06_add_bulk_items_1000.py

# 收到空白內容 (Cached)
python3 dynamodb_15_query_item_with_dax.py

# 收到內容 (after 5 mins ...)
python3 dynamodb_15_query_item_with_dax.py

# 刪除 Table 
python3 dynamodb_10_delete_table.py

# 所有查詢都可利用 DAX 
DAX_ENDPOINT='daxs://dax-cluster-demo-001.pmu19g.dax-clusters.us-east-2.amazonaws.com'
python3 dynamodb_07_get_item.py $DAX_ENDPOINT


===== 資源清理 =====

# 清理
EC2 
DAX - Cluster 
DAX - Subnet Group
DynamoDB Table
VPC 
IAM Role 
