
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/activity_task_state

# 建立 Activity Task State 
 - name: "code-review-activity"

# 建立 State Machine 
 - add 'Run Activity' Task State 
  - update name: "Waiting for Code Review"
 - click 'Choose activity'  
 - click 'Create' 

# 執行 State Machine 
 - input: 
=====
{
  "line_of_code": 5
}
===== 
 - 等待 Activity Worker 去執行 

# 建立 Lambda IAM Role
 - use case: Lambda    
 - policy: AWSStepFunctionsFullAccess, CloudWatchFullAccessV2
 - name: "role-for-lambda-activity-worker"

# 建立 Lambda Worker 
 - name: "code-reviewer-001"
 - runtime: python 
 - pick role: "role-for-lambda-activity-worker"
 - configurtion >> general configuration >> timeout: 3 min 
 - code: activity_worker.py 
  - zoom in for recording (*****)
  - update Activity Arn 
   click state >> Definition >> Activity Arn 
  - click 'Deploy'

# 執行 Lambda - Success case 
 - click Test tab >> 'Test'   
 - check state machine execution 
 - go back check labmda test logs 

---

# 建立 EventBridge 
 - name: "cr-reviewer-every-Xminutes"
 - occurence: Recurring schedule 
 - schedule type: Rate-based schedule 
  - 1 min 
 - Flexible time window 
 - Target: Lambda 
  - pick lambda function: "activity-worker-001"
 - next next
 - Create 

# 檢查 Lambda Log 
 - click Monitor >> CloudWatch Logs >> Recent invocations 

# 執行 State Machine 
 - input: 
=====
{
  "line_of_code": 10
}
===== 
 - 等待 Activity Worker 去執行 

# 檢查 Lambda Log 

# 資源清理 
 - Lambda Function 
 - IAM Role 
 - EventBridge Schedule 
 - Step Function State Machine 
 - Step Function Activity 
