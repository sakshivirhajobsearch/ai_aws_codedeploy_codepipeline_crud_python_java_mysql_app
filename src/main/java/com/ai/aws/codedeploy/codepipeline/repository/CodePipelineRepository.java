package com.ai.aws.codedeploy.codepipeline.repository;

import java.util.List;
import java.util.stream.Collectors;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.codepipeline.CodePipelineClient;
import software.amazon.awssdk.services.codepipeline.model.GetPipelineRequest;
import software.amazon.awssdk.services.codepipeline.model.GetPipelineResponse;
import software.amazon.awssdk.services.codepipeline.model.ListPipelinesResponse;
import software.amazon.awssdk.services.codepipeline.model.PipelineDeclaration;
import software.amazon.awssdk.services.codepipeline.model.PipelineSummary;

public class CodePipelineRepository {

	private final CodePipelineClient client;

	public CodePipelineRepository() {
		client = CodePipelineClient.builder().region(Region.AP_SOUTH_1) // Change to your region
				.credentialsProvider(ProfileCredentialsProvider.create()).build();
	}

	// List all pipelines
	public List<String> listPipelines() {
		ListPipelinesResponse response = client.listPipelines();
		return response.pipelines().stream().map(PipelineSummary::name).collect(Collectors.toList());
	}

	// Get pipeline details
	public PipelineDeclaration getPipeline(String pipelineName) {
		GetPipelineRequest request = GetPipelineRequest.builder().name(pipelineName).build();
		GetPipelineResponse response = client.getPipeline(request);
		return response.pipeline();
	}

	// Close client
	public void close() {
		client.close();
	}
}