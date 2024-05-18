
# 專案目錄 
https://github.com/uopsdod/aws-serverless-course/tree/main/stepfunction_demo/activity_task_state

# 建立 Activity Task State 
 - name: "activity-001"

# 建立 State Machine 
 - add 'Run Activity' Task State 
  - update name: "Waiting for Code Review"
 - enter activity arn 
 - Error Handling >> Timeout: get from input: "$.task_timeout"
 - Error Handling >> Add Retry: "States.Timeout"
 - Error Handling >> Add Retry: "States.TaskFailed"
 - click 'Create' 

# 執行 State Machine 
 - input: 
=====
{
  "line_of_code": 5,
  "task_timeout": 20
}
===== 
 - 等待 Activity Worker 去執行 

# 建立 Lambda IAM Role
 - use case: AWSStepFunctionsFullAccess, CloudWatchFullAccessV2 
 - policy: Step Function 
 - name: "role-for-lambda-activity-worker"

# 建立 Lambda Worker 
 - name: "activity-worker-001"
 - runtime: python 
 - pick role: "role-for-lambda-activity-worker"
 - configurtion >> general configuration >> timeout: 3 min 
 - code: activity_worker.py 
  - zoom in for recording (*****)
  - update Activity Arn 
  - click 'Deploy'

# 執行 Lambda - Success case 
 - click 'Test'   
 - check state machine execution 
 - go back check labmda test logs 

---

# 執行 State Machine 
 - input: 
=====
{
  "line_of_code": 5,
  "task_timeout": 20
}
===== 
 - 等待 Activity Worker 去執行 

# 執行 Lambda - Failed case 
 - update is_accept_to_review_code to False
 - click 'Deploy'
 - click 'Test'   
 - check state machine execution >> Retry 

# 執行 Lambda - Timeout case 
 - update is_accept_to_review_code to True
 - update code_review_speed to 5 
 - click 'Deploy'
 - click 'Test'   
 - check state machine execution >> Retry 

# 執行 Lambda - Success case 
 - update code_review_speed to 2 
 - click 'Deploy'
 - click 'Test'   
 - check state machine execution >> Retry 

# 資源清理 
 - Step Function State Machine 
  - you need to stop any Running state machine execution first 
 - Step Function Activity 
 - Lambda 
 - IAM Role 
