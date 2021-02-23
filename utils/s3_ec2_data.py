import os
import boto3

from dotenv import load_dotenv
load_dotenv(verbose=True)


def aws_session(region_name = "eu-west-0"):
    session = boto3.session.Session()
    return session.resource(aws_access_key_id=os.getenv('OBS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('OBS_ACCESS_KEY_SECRET'),
    service_name = "s3",
    region_name=region_name,
    use_ssl = False,
    verify=False,
    endpoint_url='http://oss.eu-west-0.prod-cloud-ocb.orange-business.com')

def make_bucket(name):
    session = aws_session()
    return session.create_bucket(Bucket=name)


def upload_file_to_bucket(bucket_name, file_path):
    session = aws_session()
    file_dir, file_name = os.path.split(file_path)

    bucket = session.Bucket(bucket_name)
    bucket.upload_file(
      Filename=file_path,
      Key=file_name,
      ExtraArgs={'ACL': 'public-read'}
    )
    s3_url = f"https://{bucket_name}.oss.eu-west-0.prod-cloud-ocb.orange-business.com/{file_name}"
    return s3_url


def download_file_from_bucket(bucket_name, s3_key, dst_path):
    session = aws_session()
    bucket = session.Bucket(bucket_name)
    bucket.download_file(Key=s3_key, Filename=dst_path)