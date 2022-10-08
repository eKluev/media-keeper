import os


class BaseSettings:
    service_name: str = 's3'
    region_name: str = os.environ.get('REGION')
    endpoint_url: str = os.environ.get('S3_ENDPOINT')
    aws_access_key_id: str = os.environ.get('ACCESS')
    aws_secret_access_key: str = os.environ.get('SECRET')
    bucket = os.environ.get('BUCKET')
    acl = 'public-read'
