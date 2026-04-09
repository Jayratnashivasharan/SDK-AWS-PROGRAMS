# main.py

from create_ec2 import create_instances
from create_load_balancer import create_load_balancer, create_target_group, create_listener
from register_targets import register_targets

def main():
    print("Creating EC2 Instances...")
    instances = create_instances()

    print("Creating Load Balancer...")
    lb_arn = create_load_balancer()

    print("Creating Target Group...")
    tg_arn = create_target_group()

    print("Registering Targets...")
    register_targets(tg_arn, instances)

    print("Creating Listener...")
    create_listener(lb_arn, tg_arn)

    print("Setup Complete!")

main();