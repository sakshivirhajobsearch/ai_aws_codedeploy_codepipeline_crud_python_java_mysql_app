package com.ai.aws.codedeploy.codepipeline.repository;

import java.util.List;
import java.util.stream.Collectors;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.codedeploy.CodeDeployClient;
import software.amazon.awssdk.services.codedeploy.model.DeploymentInfo;
import software.amazon.awssdk.services.codedeploy.model.GetDeploymentRequest;
import software.amazon.awssdk.services.codedeploy.model.GetDeploymentResponse;
import software.amazon.awssdk.services.codedeploy.model.ListDeploymentsRequest;
import software.amazon.awssdk.services.codedeploy.model.ListDeploymentsResponse;

public class CodeDeployRepository {

	private final CodeDeployClient client;

	public CodeDeployRepository() {
		client = CodeDeployClient.builder().region(Region.AP_SOUTH_1) // Change to your region
				.credentialsProvider(ProfileCredentialsProvider.create()).build();
	}

	// List all deployments
	public List<String> listDeployments(String applicationName) {
		ListDeploymentsRequest request = ListDeploymentsRequest.builder().applicationName(applicationName).build();
		ListDeploymentsResponse response = client.listDeployments(request);
		return response.deployments().stream().collect(Collectors.toList());
	}

	// Get deployment details
	public DeploymentInfo getDeployment(String deploymentId) {
		GetDeploymentRequest request = GetDeploymentRequest.builder().deploymentId(deploymentId).build();
		GetDeploymentResponse response = client.getDeployment(request);
		return response.deploymentInfo();
	}

	// Close client
	public void close() {
		client.close();
	}
}