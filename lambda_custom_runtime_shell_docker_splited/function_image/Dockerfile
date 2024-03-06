# Using an AWS OS-only base image
# ref: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#runtimes-images-provided
FROM shell-runtime-for-lambda

# copy function code to the lambda root path
COPY function.sh ${LAMBDA_TASK_ROOT}
RUN chmod 755 ${LAMBDA_TASK_ROOT}/function.sh

# specify your handler [filename].[methodname]
CMD [ "function.handler" ]