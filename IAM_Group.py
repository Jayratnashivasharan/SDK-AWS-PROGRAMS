import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')

group_name = "DevelopersGroup"

try:
    # Create IAM Group
    iam.create_group(GroupName=group_name)
    print(f"IAM Group '{group_name}' created successfully.")

    # Attach policy (Example: EC2 Read Only)
    iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
    )
    print("Policy attached to group successfully.")

except ClientError as e:
    print("Error:", e)