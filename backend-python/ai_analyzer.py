import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

# Load AWS credentials from .env
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")  # optional
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")


def validate_credentials():
    """Check if AWS credentials are valid."""
    try:
        sts = boto3.client(
            'sts',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            aws_session_token=AWS_SESSION_TOKEN if AWS_SESSION_TOKEN else None,
            region_name=AWS_REGION
        )
        identity = sts.get_caller_identity()
        print(f"✅ AWS Credentials valid. Account: {identity['Account']}, UserID: {identity['UserId']}")
        return True
    except (NoCredentialsError, PartialCredentialsError, ClientError) as e:
        print(f"❌ Invalid AWS credentials: {e}")
        return False


def get_codedeploy_client():
    return boto3.client(
        'codedeploy',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        aws_session_token=AWS_SESSION_TOKEN if AWS_SESSION_TOKEN else None,
        region_name=AWS_REGION
    )


def get_codepipeline_client():
    return boto3.client(
        'codepipeline',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        aws_session_token=AWS_SESSION_TOKEN if AWS_SESSION_TOKEN else None,
        region_name=AWS_REGION
    )


def list_codedeploy_deployments():
    client = get_codedeploy_client()
    try:
        response = client.list_deployments()
        deployments = response.get("deployments", [])
        print(f"CodeDeploy Deployments ({len(deployments)}): {deployments}")
        return deployments
    except ClientError as e:
        print(f"Error listing CodeDeploy deployments: {e}")
        return []


def list_codepipeline_pipelines():
    client = get_codepipeline_client()
    try:
        response = client.list_pipelines()
        pipelines = response.get("pipelines", [])
        print(f"CodePipeline Pipelines ({len(pipelines)}): {[p['name'] for p in pipelines]}")
        return pipelines
    except ClientError as e:
        print(f"Error listing CodePipeline pipelines: {e}")
        return []


if __name__ == "__main__":
    print("=== AI Analyzer: AWS Deployment & Pipeline Info ===\n")
    if validate_credentials():
        list_codedeploy_deployments()
        print()
        list_codepipeline_pipelines()
    else:
        print("\nPlease fix your AWS credentials in the .env file or via environment variables.")
