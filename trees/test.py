from aws_cdk.core import App, Stack
from aws_cdk import aws_s3 as s3

class HelloCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        s3.Bucket(self, "MyFirstBucket", versioned=True)

app = core.App()
HelloCdkStack(app, "HelloCdkStack")