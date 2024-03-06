# Using an AWS OS-only base image
# ref: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#runtimes-images-provided
FROM public.ecr.aws/lambda/provided:al2023

# copy runtime 
COPY bootstrap /bin
RUN chmod 755 /bin/bootstrap

# start your runtime 
ENTRYPOINT [ "/bin/bootstrap" ]