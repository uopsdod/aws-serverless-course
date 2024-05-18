import json
import boto3
import time

def lambda_handler(event, context):
    stepfunctions = boto3.client('stepfunctions')
    activity_arn = 'arn:aws:states:us-east-1:659104334423:activity:activity-001'
    code_review_speed = 2 # 0 be the fatest 
    is_accept_to_review_code = True

    try:
        response = stepfunctions.get_activity_task(
            activityArn=activity_arn,
            workerName='Code Reviewer'
        )
        
        if 'taskToken' in response:
            print(f"Found Code Review request! - taskToken: {response['taskToken']}")
            print(f"Found Code Review request! - input: {response['input']}")
            print(f"Your colleague is taking a look at your code ... ")
        
            if is_accept_to_review_code:
                print(f"Your colleague accepts to review your code.")
                activity_input = json.loads(response['input'])    
                activity_output = doing_code_review(activity_input, code_review_speed)
                stepfunctions.send_task_success(
                    taskToken=response['taskToken'],
                    output=json.dumps(activity_output)
                )
                print(f"Code Review is fininshed")
            else:
                print(f"Your colleague declines to review your code. ")
                stepfunctions.send_task_failure(
                    taskToken=response['taskToken']
                )
        else: 
            print(f"No Code Review found")
    except Exception as e:
        print(f"Error found: {str(e)}")

def doing_code_review(activity_input, code_review_speed):
    start_time = time.time()
    line_of_code = activity_input.get('line_of_code', [])
    print(f"line of code: {line_of_code}")
    
    time.sleep(code_review_speed * line_of_code)  # Simulate Code Review time 
    
    # Calculate duration in seconds 
    end_time = time.time()
    code_review_time = int(end_time - start_time)
    print(f"Code Review Time: {code_review_time} seconds")
    
    return {
        'code_review_time': code_review_time,
        'line_of_code': line_of_code
    }
