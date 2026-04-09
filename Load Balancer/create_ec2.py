import boto3
from config import *

# ✅ EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

def create_instances():
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=2,
        MinCount=2,
        SecurityGroupIds=[SECURITY_GROUP_ID],
        SubnetId=SUBNETS[0],
        UserData='''#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "<h1>Load Balancer Working</h1>" > /var/www/html/index.html
''',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'MyEC2Instance'}]
            }
        ]
    )

    instance_ids = [instance['InstanceId'] for instance in response['Instances']]
    print("EC2 Instances Created:", instance_ids)

    # ✅ Wait until running
    print("Waiting for instances to be running...")
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)

    print("Instances are now running!")

    return instance_ids