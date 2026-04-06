import boto3
import time
from botocore.exceptions import ClientError

region = "ap-south-1"
ami_id = "ami-0f5ee92e2d63afc18"  # Mumbai Amazon Linux
instance_type = "t3.micro"
key_name = "key1"

ec2 = boto3.resource('ec2', region_name=region)

def launch_instance():
    try:
        instances = ec2.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1
        )
        instance = instances[0]
        print("🚀 Launching Instance:", instance.id)

        instance.wait_until_running()
        instance.reload()

        print("✅ Running | Public IP:", instance.public_ip_address)
        return instance.id

    except ClientError as e:
        print("❌ Launch Error:", e)
        return None

def stop_instance(instance_id):
    try:
        instance = ec2.Instance(instance_id)
        instance.stop()
        instance.wait_until_stopped()
        print("🛑 Instance stopped")
    except ClientError as e:
        print("❌ Stop Error:", e)

def start_instance(instance_id):
    try:
        instance = ec2.Instance(instance_id)
        instance.start()
        instance.wait_until_running()
        print("✅ Instance started")
    except ClientError as e:
        print("❌ Start Error:", e)

def terminate_instance(instance_id):
    try:
        instance = ec2.Instance(instance_id)
        instance.terminate()
        print("🔥 Instance terminated")
    except ClientError as e:
        print("❌ Terminate Error:", e)

if __name__ == "__main__":
    instance_id = launch_instance()

    if instance_id:
        time.sleep(5)
        stop_instance(instance_id)

        time.sleep(5)
        start_instance(instance_id)

        time.sleep(5)
        terminate_instance(instance_id)