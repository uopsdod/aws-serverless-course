# Using an AWS OS-only base image
# ref: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#runtimes-images-provided
FROM public.ecr.aws/lambda/provided:al2023

# copy runtime to the layer path
# ref: https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html
COPY bootstrap /bin
RUN chmod 755 /bin/bootstrap

# copy function code to the lambda root path
COPY function.sh ${LAMBDA_TASK_ROOT}
RUN chmod 755 ${LAMBDA_TASK_ROOT}/function.sh
ENV _HANDLER=function.handler

# start your runtime 
ENTRYPOINT [ "/bin/bootstrap" ]
