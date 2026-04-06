import boto3

region = 'ap-south-1'
s3_client = boto3.client('s3', region_name=region)

s3_client.create_bucket(
    Bucket='sdkbucketzeal12345',
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)
