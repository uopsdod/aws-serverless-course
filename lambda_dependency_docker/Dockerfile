FROM public.ecr.aws/lambda/python:3.12

# Install Dependency
RUN pip install requests

# Copy function code
COPY lambda_function_only.py ${LAMBDA_TASK_ROOT}

# Set Handler [filename].[methodname]
CMD [ "lambda_function_only.handler" ]