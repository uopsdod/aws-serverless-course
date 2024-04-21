===== EC2 Linux 共用環境 =====
# 建立 VPC 
- select "VPC and more"
- name: "vpc-api-001"

# 建立 IAM Role for EC2
- name: "api-ec2-role-001"
- policy: "AdministratorAccess"

# 建立 EC2 Instance 
- name: "api-ec2-001"
- no key pair 
- vpc: "vpc-api-001"
- subnet: pick public ones
- enable public ip 
- click Advanced setting
 - pick role "api-ec2-role-001"
