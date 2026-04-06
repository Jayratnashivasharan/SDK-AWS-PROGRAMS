import boto3
import os
from botocore.exceptions import ClientError

bucket_name = "sdkbucketzeal12345"
file_path = r"J:\sdk\test.txt"
s3_key = "test.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def upload():
    if not os.path.exists(file_path):
        print("❌ File not found:", file_path)
        return

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print("✅ File uploaded successfully.")
    except ClientError as e:
        print("❌ Upload Error:", e.response['Error']['Message'])

if __name__ == "__main__":
    upload()