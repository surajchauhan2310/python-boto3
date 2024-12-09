import boto3
import boto3.session

# Use the "devops" profile
session = boto3.session.Session(profile_name="devops")

# Create an S3 client
client = session.client("s3")

# Specify the bucket name
bucket_name = "my-aws-bucket1"  # Replace with a globally unique bucket name

# Correct the bucket creation logic
try:
    response = client.create_bucket(
        Bucket="my-bucket-dim-0712",
        CreateBucketConfiguration={
            'LocationConstraint': session.region_name  # Add location constraint dynamically
        }
    )
    print("Bucket created successfully:", response)
except client.exceptions.ClientError as e:
    print("Error:", e)


import boto3
import boto3.session

# Use the "devops" profile
session = boto3.session.Session(profile_name="devops")

# Create an S3 client
client = session.client("s3")

# Specify the bucket name
bucket_name = "my-aws-bucket1"  # Replace with a globally unique bucket name

# Correct the bucket creation logic
try:
    response = client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': session.region_name  # Add location constraint dynamically
        }
    )
    print("Bucket created successfully:", response)
except client.exceptions.ClientError as e:
    print("Error:", e)

import boto3
import boto3.session

# Use the "devops" profile
session = boto3.session.Session(profile_name="devops")

# Create an S3 client
client = session.client("s3")

# Specify the bucket name
# bucket_name = "my-aws-bucket1"  # Replace with a globally unique bucket name

# Correct the bucket creation logic
# try:
#     response = client.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#             'LocationConstraint': session.region_name  # Add location constraint dynamically
#         }
#     )
#     print("Bucket created successfully:", response)
# except client.exceptions.ClientError as e:
#     print("Error:", e)
response1 = client.list_buckets()
       
print(response1)