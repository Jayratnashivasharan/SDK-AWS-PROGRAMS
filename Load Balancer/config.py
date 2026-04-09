# config.py

REGION = "ap-south-1"  # Mumbai region
AMI_ID = "ami-0f5ee92e2d63afc18"  # Amazon Linux 2
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "key1"

SECURITY_GROUP_ID = "sg-0ae062a29a77a3534"
SUBNETS = ["subnet-055ebec69abf12326", "subnet-037a762cdfca4a532"]  # 2 subnets required for ALB

VPC_ID = "vpc-06c2e9e4c9cd3a11a"

LOAD_BALANCER_NAME = "my-load-balancer-1"
TARGET_GROUP_NAME = "my-target-group-1"