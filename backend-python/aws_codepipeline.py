import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")


def get_codepipeline_client():
    return boto3.client(
        'codepipeline',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        aws_session_token=AWS_SESSION_TOKEN if AWS_SESSION_TOKEN else None,
        region_name=AWS_REGION
    )


def list_pipelines():
    client = get_codepipeline_client()
    try:
        response = client.list_pipelines()
        return response['pipelines']
    except ClientError as e:
        return f"ClientError: {e}"
