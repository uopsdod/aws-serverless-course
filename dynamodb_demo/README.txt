===== EC2 Linux 共用環境 =====
# 建立 VPC 
- select "VPC and more"
- name: "vpc-dynamodb-001"

# 建立 IAM Role for EC2
- name: "dynamodb-ec2-role-001"
- policy: "AmazonDynamoDBFullAccess"

# 建立 EC2 Instance 
- name: "dynamodb-ec2-001"
- no key pair 
- vpc: "vpc-dynamodb-001"
- subnet: pick public ones
- enable public ip 
- click Advanced setting
 - pick role "dynamodb-ec2-role-001"

===== Console 操作 ===== 

# 建立 Table 
table name: "game-001"
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

click [item02] -> Action -> duplicate item
 [item02]
 - Number:hour: 12
 - String:type: poker
 - Number:duration: 312
 - String:winner: yoyodi
 - String Set:players: "harry", "zebie", "yoyodi"
 - Boolean:is_vip: True 

click [item03] -> Action -> duplicate item
 [item03]
 - Number:hour: 14
 - String:type: tennis
 - Number:duration: 700
 - String:winner: kkdd303
 - String Set:players: "kkdd303", "zebie", "yoyodi"
 - String:is_vip: false

# 更新 Item  
click [item01] -> Action -> Edit item 
 - Number:duration: 501

# 刪除 Item 
click [item03] -> Action -> delete item 

# 讀取單一 Item 

# 搜尋 Query Items
 - 查看 Read Capacity 用量
 - 限制: 無法查詢 is_vip 欄位 

# 搜尋 Scan Items 
 - 查看 Read Capacity 用量

# 刪除 Table
 

===== Python 程式碼操作 =====

# 進入 EC2 Instance 

# 下載專案
sudo yum install -y git
git clone https://github.com/uopsdod/aws-serverless-course.git

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax

# 安裝第三方套件
sudo yum install -y pip
pip3 install boto3

# 建立 Table 
python3 dynamodb_01_create_table.py

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax

# 建立 Item 
python3 dynamodb_02_add_items.py

# 更新 Item  
python3 dynamodb_03_update_items.py

# 刪除 Item 
python3 dynamodb_04_delete_items.py

# 建立 Multiple Items 
python3 dynamodb_05_add_items_1000.py
python3 dynamodb_06_add_bulk_items_1000.py 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax

# 讀取單一 Item 
python3 dynamodb_07_get_item.py

# 搜尋 Query Items
python3 dynamodb_08_query_item.py

# 搜尋 Scqn Items 
python3 dynamodb_09_scan_item.py

# 刪除 Table (optional)
python3 dynamodb_demo/basic/dynamodb_10_delete_table.py

===== 建立 Secondary Index ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/secondary_index

# 建立 base table + LSI 
python3 dynamodb_01_create_table_with_lsi.py
python3 dynamodb_02_add_bulk_items_1000.py

# 使用 LSI 
python3 dynamodb_03_query_item_with_lsi.py

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/secondary_index

# 建立 GSI 
python3 dynamodb_04_create_gsi.py

# 使用 GSI 
python3 dynamodb_05_query_item_with_gsi.py

# 刪除 base table + LSI + GSI (optional)
python3 dynamodb_06_delete_table_with_lsi.py

===== 建立 DAX ===== 

# 建立 Security Group
- name: "dynamodb-dax-sg-001"
- description: "dynamodb-dax-sg-001"
- vpc: "vpc-dynamodb-001"
- description: "dynamodb-dax-001"
- port: 8111
- port: 9111 

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
 - policy name: "DAXFullAccess-dax-to-dynamodb-role-001"
- Parameter Group
 - name: "dax-parameter-group-001"
 - TTL: Item time-to-live (TTL) set to 1 minute
 - TTL: Query time-to-live (TTL) set to 1 minute 

===== 使用 DAX - Cache 機制示範 ===== 

# 進入 EC2 Instance 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax

# 安裝第三方套件
pip3 install boto3
pip3 install amazon-dax-client

# 設定 DAX Endpoint 環境參數 
DAX_ENDPOINT='daxs://dax-cluster-demo-001.pmu19g.dax-clusters.us-east-2.amazonaws.com'

# 建立 Table (no need anymore, cuz I didn't delete tables before at all)
python3 dynamodb_01_create_table.py
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT

# 查詢到內容
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 刪除 Table 
python3 dynamodb_10_delete_table.py

# 仍然收到內容 (Cached) 
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 收到錯誤訊息 (after 5 mins ...)
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 建立 Table 
python3 dynamodb_01_create_table.py 

# 收到空內容 
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 建立測試資料
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT

# 收到空內容 (Cached)
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 收到內容 (after 5 mins ...)
python3 dynamodb_08_query_item.py $DAX_ENDPOINT

# 刪除 Table (optional)
python3 dynamodb_10_delete_table.py

===== 使用 DAX ===== 

# Item Read/Write 都可利用 DAX 

cd ~/aws-serverless-course/dynamodb_demo/basic_with_dax
python3 dynamodb_02_add_items.py $DAX_ENDPOINT
python3 dynamodb_03_update_items.py $DAX_ENDPOINT
python3 dynamodb_04_delete_items.py $DAX_ENDPOINT
python3 dynamodb_05_add_items_1000.py $DAX_ENDPOINT
python3 dynamodb_06_add_bulk_items_1000.py $DAX_ENDPOINT
python3 dynamodb_07_get_item.py $DAX_ENDPOINT
python3 dynamodb_08_query_item.py $DAX_ENDPOINT
python3 dynamodb_09_scan_item.py $DAX_ENDPOINT

cd ~/aws-serverless-course/dynamodb_demo/secondary_index
python3 dynamodb_02_add_bulk_items_1000.py $DAX_ENDPOINT
python3 dynamodb_03_query_item_with_lsi.py $DAX_ENDPOINT
python3 dynamodb_05_query_item_with_gsi.py $DAX_ENDPOINT
 
===== Transaction =====

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/transaction

# 建立 Tables 
python3 dynamodb_01_create_table_skill.py
python3 dynamodb_02_add_items_skill.py
python3 dynamodb_03_create_table_player.py
python3 dynamodb_04_add_items_player.py

# Transaction 成功執行 
python3 dynamodb_05_add_items_in_transaction.py

# Transaction 模擬失敗狀況 
python3 dynamodb_06_add_items_in_transaction_error.py

# 刪除 Tables(optional)
python3 dynamodb_07_delete_table_skill.py
python3 dynamodb_08_delete_table_player.py

===== Versioning ===== 

# 進入本單元專案目錄
cd ~/aws-serverless-course/dynamodb_demo/versioning

# Versioning 成功執行
python3 dynamodb_01_create_table_skill_version.py
python3 dynamodb_02_add_items_skill_version.py
python3 dynamodb_03_update_item_versioning.py

# Versioning 模擬錯誤狀況 
python3 dynamodb_04_update_item_versioning_slow.py

(open the 2nd terminals)
cd ~/aws-serverless-course/dynamodb_demo/versioning
python3 dynamodb_05_update_item_versioning_slow_interrupt.py

(go back to the 1st terminal)
- expect: see version conflict error 

python3 dynamodb_06_delete_table_skill_version.py

===== 資源清理 =====

# 資源清理 (照著以下順序)
EC2 Instance 
DAX - Cluster 
DAX - Subnet Group
DynamoDB Table

VPC 

IAM Role for EC2
IAM Role for DAX 
IAM Policy for DAX 
