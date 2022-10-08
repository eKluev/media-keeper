import boto3
from app.v2.settings import BaseSettings


class Client(BaseSettings):
    def get_client(self):
        return boto3.client(service_name=self.service_name,
                            region_name=self.region_name,
                            endpoint_url=self.endpoint_url,
                            aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    def put_object(self, media, path) -> dict:
        client = self.get_client()
        client.put_object(Bucket=self.bucket,
                          Body=media,
                          Key=path,
                          ACL=self.acl)

        return self.generate_url(path)

    def delete_object(self, url) -> dict:
        file = url.split('.com/')[1]
        client = self.get_client()
        client.delete_object(Bucket=self.bucket, Key=f"{file}")
        return {"status": "ok", 'result': f'{file} has been deleted'}

    def generate_url(self, path) -> dict:
        url = {"status": "ok"}

        if 'amazonaws' in self.endpoint_url:
            # path-style access
            # url['result'] = {"url": f"https://s3.{self.region_name}.amazonaws.com/{self.bucket}/{self.path}"}

            # virtual-hosted–style access
            url['result'] = {"url": f"https://{self.bucket}.s3.{self.region_name}.amazonaws.com/{path}"}

        if 'digitaloceanspaces' in self.endpoint_url:
            url['result'] = {"url": f"https://{self.bucket}.{self.region_name}.digitaloceanspaces.com/{path}"}

        return url

