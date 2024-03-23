

# 安裝第三方套件
# - python 套件需要在 Lambda 根目錄底下
python3 -m venv venv
source venv/bin/activate
pip3 install boto3
pip3 install amazon-dax-client
ls venv/lib/python3.9/site-packages/

