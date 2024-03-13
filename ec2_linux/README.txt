# 建立基礎資源 - IAM Role for EC2
- service: EC2 
- policy: AdministratorAccess
- name: "serverless-admin-role"

# 建立基礎資源 - IAM Role for Lambda
- service: Lambda
- policy: AWSLambdaBasicExecutionRole
- name: "serverless-lambda-role"

# 建立基礎資源 - VPC
- click 'VPC and more'
- name: "serverless-vpc"

# 建立基礎資源 - EC2
- name: "serverless-ec2-demo"
- select no key pair
- select VPC
 - select public subnet
 - enable public ip 
- expand 'Advanced details'
 - select iam role "serverless-admin-role"

# 進入 EC2 

# 安裝套件 - git
sudo yum install -y git 

# 安裝套件 - docker 
sudo yum install docker -y

# 安裝套件 - python
sudo yum install -y python
sudo yum install -y pip

# 下載專案
git clone https://github.com/uopsdod/aws-serverless-course
ls
