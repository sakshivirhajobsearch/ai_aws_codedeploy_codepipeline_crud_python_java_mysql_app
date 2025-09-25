from datetime import datetime, timedelta
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION")
cd_client = boto3.client('codedeploy', region_name=region)
cp_client = boto3.client('codepipeline', region_name=region)

def analyze_deployment_failures(application_name):
    now = datetime.utcnow()
    past_24h = now - timedelta(hours=24)
    failures = []

    deployments = cd_client.list_deployments(
        applicationName=application_name,
        includeOnlyStatuses=['Failed']
    )

    for dep_id in deployments.get('deployments', []):
        info = cd_client.get_deployment(deploymentId=dep_id)
        failures.append({
            'id': dep_id,
            'status': info['deploymentInfo']['status'],
            'createTime': str(info['deploymentInfo']['createTime']),
            'message': info['deploymentInfo'].get('errorInformation', {}).get('message', 'No message')
        })

    alert = None
    if len(failures) >= 3:
        alert = f"⚠️ AI ALERT: {len(failures)} failed deployments in the last 24 hours for {application_name}!"

    return {'application': application_name, 'failures': failures, 'alert': alert}

def analyze_pipeline_failures(pipeline_name):
    executions = cp_client.list_pipeline_executions(pipelineName=pipeline_name, maxResults=10)
    failures = []

    for exe in executions.get('pipelineExecutionSummaries', []):
        if exe['status'] == 'Failed':
            failures.append({
                'id': exe['pipelineExecutionId'],
                'status': exe['status'],
                'lastUpdate': str(exe['lastUpdateTime']),
                'reason': exe.get('trigger', {}).get('triggerDetail', 'Unknown')
            })

    aler
