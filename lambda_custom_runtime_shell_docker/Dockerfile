# Using an AWS OS-only base image
# ref: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#runtimes-images-provided
FROM public.ecr.aws/lambda/provided:al2023

# copy runtime 
COPY bootstrap /bin
RUN chmod 755 /bin/bootstrap

# copy function code to the lambda root path
COPY function.sh ${LAMBDA_TASK_ROOT}
RUN chmod 755 ${LAMBDA_TASK_ROOT}/function.sh

# start your runtime 
ENTRYPOINT [ "/bin/bootstrap" ]
CMD [ "function.handler" ]