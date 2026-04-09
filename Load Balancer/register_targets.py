# register_targets.py

import boto3
from config import *

elbv2 = boto3.client('elbv2', region_name=REGION)

def register_targets(tg_arn, instance_ids):
    targets = [{'Id': i} for i in instance_ids]

    elbv2.register_targets(
        TargetGroupArn=tg_arn,
        Targets=targets
    )

    print("Instances Registered to Target Group")