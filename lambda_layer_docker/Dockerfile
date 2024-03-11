FROM public.ecr.aws/lambda/python:3.12

# Install Dependency to Layer folder
RUN pip install requests --target /opt2/python

# Copy function code
COPY lambda_function_only.py ${LAMBDA_TASK_ROOT}

# Set Handler [filename].[methodname]
CMD [ "lambda_function_only.handler" ]