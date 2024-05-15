#!/usr/bin/env python
# coding: utf-8

# In[65]:


import boto3
import uuid

# Training Sample 
# [1] the first column is target while all other columns are features 
# 0,55,95
# 0,92,73
# 0,12,25
# 0,19,28
# 1,98,25

sagemaker_client = boto3.client('sagemaker')

# Step 1: Create a Training Job
training_image_xgboost = "811284229777.dkr.ecr.us-east-1.amazonaws.com/xgboost:latest" # built-in training algo
hyper_parameter_xgboost = {
    "objective": "reg:logistic",
    "eval_metric": "rmse",
    "num_round": "5"
  }
s3_bucket_output = 'stepfunctionssample-sagemake-bucketformodelanddata-fxj6mvkkagyt'
# iam_role_sagemaker needs S3 access, SageMaker access 
iam_role_sagemaker = "arn:aws:iam::659104334423:role/StepFunctionsSample-SageM-SageMakerAPIExecutionRole-8Mj2qJNWPgHE"
training_job_name = f"MyTrainingJobName001-{str(uuid.uuid4())}"
training_params = {
  "AlgorithmSpecification": {
    "TrainingImage": training_image_xgboost,
    "TrainingInputMode": "File"
  },
  "OutputDataConfig": {
    "S3OutputPath": f"s3://{s3_bucket_output}/models"
  },
  "StoppingCondition": {
    "MaxRuntimeInSeconds": 86400
  },
  "ResourceConfig": {
    "InstanceCount": 1,
    "InstanceType": "ml.m5.xlarge",
    "VolumeSizeInGB": 30
  },
  "RoleArn": iam_role_sagemaker,
  "InputDataConfig": [
    {
      "DataSource": {
        "S3DataSource": {
          "S3DataDistributionType": "ShardedByS3Key",
          "S3DataType": "S3Prefix",
          "S3Uri": f"s3://{s3_bucket_output}/csv/train.csv"
        }
      },
      "ChannelName": "train",
      "ContentType": "text/csv"
    }
  ],
  "HyperParameters": hyper_parameter_xgboost,
  "TrainingJobName": training_job_name
}

response = sagemaker_client.create_training_job(**training_params)
print(f"Training job ARN: {response['TrainingJobArn']}")
print(f"Training job name: {training_job_name}")


# In[68]:


# Describe the training job to get details
response = sagemaker_client.describe_training_job(TrainingJobName=training_job_name)

# Extract the S3 model artifact URL
model_artifact_url = response['ModelArtifacts']['S3ModelArtifacts']
print(f'S3 Model Artifact URL: {model_artifact_url}')


# In[69]:


# Step 2: Create a Model
# [1] change the ModelDataUrl
# ModelDataUrl = 's3://stepfunctionssample-sagemake-bucketformodelanddata-fxj6mvkkagyt/models/MyTrainingJobName001-91fc9fa1-42a7-4f8f-bc79-e2a86343dd90/output/model.tar.gz'
modelName = 'my-trained-model-001'

model_params = {
    'ModelName': modelName,
    'PrimaryContainer': {
        'Image': training_image_xgboost,
        'ModelDataUrl': model_artifact_url
    },
    'ExecutionRoleArn': iam_role_sagemaker
}

response = sagemaker_client.create_model(**model_params)
print(f"Model ARN: {response['ModelArn']}")


# In[70]:


# Step 3: Deploy the Model to a Real-time Endpoint
endpointConfigName = 'my-endpoint-config-001'
endpointName = 'my-endpoint-001'

endpoint_config_params = {
    'EndpointConfigName': endpointConfigName,
    'ProductionVariants': [
        {
            'VariantName': 'AllTraffic',
            'ModelName': modelName,
            'InstanceType': 'ml.m5.xlarge',
            'InitialInstanceCount': 1
        }
    ]
}

response = sagemaker_client.create_endpoint_config(**endpoint_config_params)
print(f"Endpoint Config ARN: {response['EndpointConfigArn']}")

endpoint_params = {
    'EndpointName': endpointName,
    'EndpointConfigName': endpointConfigName
}

response = sagemaker_client.create_endpoint(**endpoint_params)
print(f"Endpoint ARN: {response['EndpointArn']}")


# In[79]:


try:
    # Describe the endpoint to get its details
    response = sagemaker_client.describe_endpoint(EndpointName=endpointName)
    
    # Extract the endpoint status
    endpoint_status = response['EndpointStatus']
    print(f'Endpoint status: {endpoint_status}')
    
    # Optionally, print more details about the endpoint
    # print(f'Endpoint details: {response}')
    
    # Check if the endpoint is in service
    if endpoint_status == 'InService':
        print(f'The endpoint {endpoint_name} is successfully created and in service.')
    elif endpoint_status == 'Creating':
        print(f'The endpoint {endpoint_name} is still being created.')
    elif endpoint_status == 'Failed':
        print(f'The creation of the endpoint {endpoint_name} has failed.')
    else:
        print(f'The endpoint {endpoint_name} is in status: {endpoint_status}')
except sagemaker_client.exceptions.ResourceNotFound:
    print(f'The endpoint {endpoint_name} does not exist.')
except Exception as e:
    print(f'Error describing the endpoint: {e}')


# In[87]:


# Step 4: Invoke the Endpoint for Real-time Predictions
runtime_client = boto3.client('sagemaker-runtime')

# Example input data based on your training input
input_data = '98,25'

# probability score that represents the likelihood of the input belonging to the positive class (in this case, class 1)
response = runtime_client.invoke_endpoint(
    EndpointName=endpointName,
    ContentType='text/csv',
    Body=input_data
)

result = response['Body'].read().decode('utf-8')
print(f'Probability predicted result: {result}')

threshold = 0.5
binary_prediction = 1 if float(result) > threshold else 0
print(f'Binary predicted result: {binary_prediction}')



# In[89]:


# Clean Up: Endpoint , Endpoint Config, Model, S3 (training.csv, test.csv, S3 model artifact, S3 model)
# Resource names 
# bucket_name = 'stepfunctionssample-sagemake-bucketformodelanddata-fxj6mvkkagyt'
output_key_prefix = 'models/'
# train_data_key = 'csv/train.csv' 



# In[90]:


import boto3

# Step 1: Delete the Endpoint
try:
    sagemaker_client.delete_endpoint(EndpointName=endpointName)
    print(f"Deleted endpoint: {endpoint_name}")
except Exception as e:
    print(f"Error deleting endpoint: {e}")


# In[91]:


# Step 2: Delete the Endpoint Configuration
try:
    sagemaker_client.delete_endpoint_config(EndpointConfigName=endpointConfigName)
    print(f"Deleted endpoint config: {endpoint_config_name}")
except Exception as e:
    print(f"Error deleting endpoint config: {e}")



# In[92]:


# Step 3: Delete the Model
try:
    sagemaker_client.delete_model(ModelName=modelName)
    print(f"Deleted model: {model_name}")
except Exception as e:
    print(f"Error deleting model: {e}")



# In[93]:


# Step 4: Clean up S3 Resources
s3_client = boto3.client('s3')
# Delete training data (skip it for now)
# try:
#     s3_client.delete_object(Bucket=bucket_name, Key=train_data_key)
#     print(f"Deleted training data: {train_data_key}")
# except Exception as e:
#     print(f"Error deleting training data: {e}")

# Delete model artifacts
try:
    response = s3_client.list_objects_v2(Bucket=s3_bucket_output, Prefix=output_key_prefix)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_client.delete_object(Bucket=s3_bucket_output, Key=obj['Key'])
            print(f"Deleted object: {obj['Key']}")
    print(f"Deleted model artifacts under prefix: {output_key_prefix}")
except Exception as e:
    print(f"Error deleting model artifacts: {e}")


# In[ ]:




