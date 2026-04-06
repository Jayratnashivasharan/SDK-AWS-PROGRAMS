import boto3
from botocore.exceptions import ClientError

bucket_name = "sdkbucketzeal12345"
s3_key = "test.txt"
download_path = r"J:\sdk\downloaded_test.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def download():
    try:
        s3.download_file(bucket_name, s3_key, download_path)
        print("✅ File downloaded successfully.")
    except ClientError as e:
        print("❌ Download Error:", e.response['Error']['Message'])

if __name__ == "__main__":
    download()