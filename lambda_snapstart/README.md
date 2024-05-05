
# 下載 mvn 
- file name: apache-maven-3.9.6-bin.zip
 - https://maven.apache.org/download.cgi

# 建立 Java 專案 
./apache-maven-3.9.6/bin/mvn archetype:generate -DgroupId=com.example -DartifactId=my-lambda-function -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

ls -lh 
 - my-lambda-function 建立 

# 新增 aws-lambda-java-core 
vi pom.xml
=====
...
<!-- AWS Lambda Java SDK -->
    <dependency>
        <groupId>com.amazonaws</groupId>
        <artifactId>aws-lambda-java-core</artifactId>
        <version>1.2.1</version> <!-- Use the latest version -->
    </dependency>
...
=====

# 新增 Lambda Handler Code 
(MyLambdaFunction.java)

# 建立 jar 部署檔案
cd my-lambda-function
mvn clean package 
ls -lh ./target
 - 看見 my-lambda-function-1.0-SNAPSHOT.jar 

# 登入 AWS 帳號
# 建立 Lambda Function 
 - name: "function-java-001"
 - runtime: Java 

# 更新 Lambda Handler Code 
# 更新 Lambda Handler 設定 
# 更新 Timeout 
# 測試 

# 啟用 SnapStart 
# 建立 Version v1 
 - see msg: "Creating version 1 of function function-java-001. SnapStart adds a few minutes to the version creation process." 

# 測試 Version v1 
 - expect: 等待 3 秒多收到回應
  - Restore Duration + Handler Duration 

# 部署 Lambda Handler Code + SnapStart Hooks 

# Maven 
mvn clean package
 - jar path: "function-sample-aws-0.0.1-SNAPSHOT-aws.jar"


