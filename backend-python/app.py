from flask import Flask, jsonify
from aws_codedeploy import list_deployments
from aws_codepipeline import list_pipelines

app = Flask(__name__)

@app.route('/codedeploy')
def codedeploy():
    deployments = list_deployments()
    return jsonify(deployments)

@app.route('/codepipeline')
def codepipeline():
    pipelines = list_pipelines()
    return jsonify(pipelines)

@app.route('/ai/deploy-alert/<app_name>')
def deploy_alert(app_name):
    # Example: trigger some alert logic
    return jsonify({"message": f"Deploy alert triggered for {app_name}"})

if __name__ == '__main__':
    app.run(debug=True)
