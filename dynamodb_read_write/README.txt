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
pip3 install amazon-dax-client

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




