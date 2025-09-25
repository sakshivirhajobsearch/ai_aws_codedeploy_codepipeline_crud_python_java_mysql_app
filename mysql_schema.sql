CREATE DATABASE IF NOT EXISTS ai_aws_codedeploy_codepipeline;
USE ai_aws_codedeploy_codepipeline;

CREATE TABLE deployments (
    id VARCHAR(100) PRIMARY KEY,
    status VARCHAR(50),
    appName VARCHAR(100)
);

CREATE TABLE pipelines (
    name VARCHAR(100) PRIMARY KEY,
    version INT
);
