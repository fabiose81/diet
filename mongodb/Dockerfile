FROM mongo:7.0

# Install Python 3.11 and pip (required by Fargate for EFS mount)
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip curl && \
    ln -s /usr/bin/python3.11 /usr/bin/python && \
    pip3 install --upgrade pip boto3 botocore && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
 
WORKDIR /data

# Set environment variables
ARG DATABASE
ENV MONGO_INITDB_DATABASE=$DATABASE

# Expose MongoDB port
EXPOSE 27017

# Optional: define default command (MongoDB image already has one)
CMD ["mongod"]