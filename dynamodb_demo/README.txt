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

# 讀取單一 Item 

# 搜尋 Query Items
 - 查看 Read Capacity 用量
 - 限制: 無法查詢 is_vip 欄位 

# 搜尋 Scqn Items 
 - 查看 Read Capacity 用量

# 刪除 Table
 

===== Python 程式碼操作 =====

# 下載專案
git clone https://github.com/uopsdod/aws-serverless-course.git

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax

# 安裝第三方套件
# - python 套件需要在 Lambda 根目錄底下
python3 -m venv venv
source venv/bin/activate
pip3 install boto3

# 建立 Table 
python3 dynamodb_01_create_table.py

# 建立 Item 
python3 dynamodb_02_add_items.py

# 更新 Item  
python3 dynamodb_03_update_items.py

# 刪除 Item 
python3 dynamodb_04_delete_items.py

# 建立 Multiple Items 
python3 dynamodb_05_add_items_1000.py
python3 dynamodb_06_add_bulk_items_1000.py 

# 讀取單一 Item 
python3 dynamodb_07_get_item.py

# 搜尋 Query Items
python3 dynamodb_08_query_item.py

# 搜尋 Scqn Items 
python3 dynamodb_09_scan_item.py

# 刪除 Table
python3 dynamodb_demo/basic/dynamodb_10_delete_table.py

===== 建立 Secondary Index ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/secondary_index

# 建立 base table + LSI 
python3 dynamodb_01_create_table_with_lsi.py
python3 dynamodb_02_add_bulk_items_1000.py

# 使用 LSI 
python3 dynamodb_03_query_item_with_lsi.py

# 建立 GSI 
python3 dynamodb_04_create_gsi.py

# 使用 GSI 
python3 dynamodb_05_query_item_with_gsi.py

# 刪除 base table + LSI + GSI 
python3 dynamodb_06_delete_table_with_lsi.py

===== 建立 DAX ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic

# 安裝第三方套件
pip3 install amazon-dax-client

# 建立 VPC 
- select "VPC and more"
- name: "vpc-dynamodb-001"

# 建立 Security Group
- name: "dynamodb-dax-sg-001"
- description: "dynamodb-dax-sg-001"
- vpc: "vpc-dynamodb-001"
- description: "dynamodb-dax-001"
- port: 8111
- port: 9111 

# 建立 IAM Role for DAX 
- Service: DynamoDB
 - Use Case: Amazon DynamoDB Accelerator (DAX) - DynamoDB access
- name: "dax-to-dynamodb-role-001"

# 建造 DAX Cluster 
- cluster name: "dax-cluster-001" 
- Node family: t-type family
- # of nodes: 3
- create a subnet Group: "subnet-group-001"
 - pick VPC "vpc-dynamodb-001"
  - pick any 2 subnets 
  - pick security Group "dynamodb-dax-sg-001"
- create an IAM role: 
 - name: "dax-to-dynamodb-role-001"
- Parameter Group
 - TTL: Item time-to-live (TTL)
 - TTL: Query time-to-live (TTL)

# 建立 IAM Role for EC2
- name: "dynamodb-dax-ec2-role"

# 建立 EC2 Instance 

# 進入 EC2 Instance 

===== 使用 DAX - 模擬 Cache 機制 ===== 

# 設定 DAX Endpoint 環境參數
DAX_ENDPOINT='daxs://dax-cluster-demo-001.pmu19g.dax-clusters.us-east-2.amazonaws.com'

# 建立 Table 
python3 dynamodb_01_create_table.py
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT

# 查詢到內容
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 刪除 Table 
python3 dynamodb_10_delete_table.py

# 收到錯誤
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 建立 Table 
python3 dynamodb_01_create_table.py 

# 收到空白內容 
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 建立測試資料
python3 dynamodb_06_add_bulk_items_1000.py 

# 收到空白內容 (Cached)
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 收到內容 (after 5 mins ...)
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 刪除 Table 
python3 dynamodb_10_delete_table.py

===== 使用 DAX ===== 

# Item Read/Write 都可利用 DAX 

python3 dynamodb_01_create_table.py
python3 dynamodb_02_add_items.py $DAX_ENDPOINT
python3 dynamodb_03_update_items.py $DAX_ENDPOINT
python3 dynamodb_04_delete_items.py $DAX_ENDPOINT
python3 dynamodb_05_add_items_1000.py $DAX_ENDPOINT
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT
python3 dynamodb_07_get_item.py $DAX_ENDPOINT
python3 dynamodb_08_query_item.py $DAX_ENDPOINT
python3 dynamodb_09_scan_item.py $DAX_ENDPOINT
python3 dynamodb_10_delete_table.py
python3 dynamodb_11_create_table_with_lsi.py 
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT
python3 dynamodb_12_query_item_with_lsi.py $DAX_ENDPOINT
python3 dynamodb_13_create_gsi.py 
python3 dynamodb_14_query_item_with_gsi.py $DAX_ENDPOINT
python3 dynamodb_10_delete_table.py

===== Transaction =====

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/transaction

# Transaction 
python3 dynamodb_15_create_table_skill.py
python3 dynamodb_16_add_items_skill.py
python3 dynamodb_17_create_table_player.py
python3 dynamodb_18_add_items_player.py
python3 dynamodb_19_add_items_in_transaction.py
python3 dynamodb_20_delete_table_skill.py
python3 dynamodb_21_delete_table_player.py


===== Versioning ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/versioning

# Versioning 
python3 versioning/dynamodb_22_create_table_skill_version.py
python3 versioning/dynamodb_23_add_items_skill_version.py
python3 versioning/dynamodb_24_versioning.py

(open the 2nd terminals)
python3 -m venv venv
source venv/bin/activate
pip3 install boto3
cd versioning/
python3 versioning/dynamodb_25_versioning_interrupt.py

(check version on Console)
(go back to the 1st terminal)
- expect: see version conflict error 

===== 資源清理 =====

# 清理 
EC2 
DAX - Cluster 
DAX - Subnet Group
DynamoDB Table
VPC 
IAM Role 
