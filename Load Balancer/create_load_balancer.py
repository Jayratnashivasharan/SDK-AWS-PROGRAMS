# create_load_balancer.py

import boto3
from config import *

elbv2 = boto3.client('elbv2', region_name=REGION)

def create_load_balancer():
    response = elbv2.create_load_balancer(
        Name=LOAD_BALANCER_NAME,
        Subnets=SUBNETS,
        SecurityGroups=[SECURITY_GROUP_ID],
        Scheme='internet-facing',
        Type='application',
        IpAddressType='ipv4'
    )

    lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
    print("Load Balancer ARN:", lb_arn)

    return lb_arn


def create_target_group():
    response = elbv2.create_target_group(
        Name=TARGET_GROUP_NAME,
        Protocol='HTTP',
        Port=80,
        VpcId=VPC_ID,
        TargetType='instance'
    )

    tg_arn = response['TargetGroups'][0]['TargetGroupArn']
    print("Target Group ARN:", tg_arn)

    return tg_arn


def create_listener(lb_arn, tg_arn):
    response = elbv2.create_listener(
        LoadBalancerArn=lb_arn,
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': tg_arn
            }
        ]
    )

    print("Listener Created")