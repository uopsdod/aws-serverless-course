FROM public.ecr.aws/lambda/python:3.12

# Install Extension to Layer Extension folder 
COPY ./extensions /opt/extensions
RUN cd /opt/extensions && chmod +x python-example-extension
COPY ./python-example-extension /opt/python-example-extension
RUN cd /opt/python-example-extension && chmod +x extension.py
RUN cd /opt/python-example-extension && pip3 install -r requirements.txt -t .

# Install Dependency to Layer folder
RUN pip install requests --target /opt/python

# Copy function code
COPY lambda_function_only.py ${LAMBDA_TASK_ROOT}

# Set Handler [filename].[methodname]
CMD [ "lambda_function_only.handler" ]