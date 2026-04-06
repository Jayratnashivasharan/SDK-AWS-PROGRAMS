import boto3
from botocore.exceptions import ClientError

# Create IAM client
iam = boto3.client('iam')

user_name = "SDKUserEC2Access"

try:
    # 1. Create IAM User
    response = iam.create_user(
        UserName=user_name
    )
    print(f"IAM User '{user_name}' created successfully.")

    # 2. Attach EC2 Full Access Policy
    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonEC2FullAccess"
    )
    print("AmazonEC2FullAccess policy attached successfully.")

except ClientError as e:
    print("Error:", e)