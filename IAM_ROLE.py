import boto3
import json
from botocore.exceptions import ClientError  # ✅ FIX 1: Import added

# ✅ FIX 2: Create IAM client
iam = boto3.client('iam')

role_name = "EC2AccessRole"

assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

try:
    # Create IAM Role
    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )
    print(f"IAM Role '{role_name}' created successfully.")

    # Attach Policy
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonEC2FullAccess"
    )
    print("Policy attached successfully.")

except ClientError as e:
    print("Error:", e)