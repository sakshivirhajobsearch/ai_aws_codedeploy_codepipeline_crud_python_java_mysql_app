package com.ai.aws.codedeploy.codepipeline.gui;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import com.ai.aws.codedeploy.codepipeline.utility.HttpClientHelper;

// http://127.0.0.1:5000/codedeploy
// http://127.0.0.1:5000/codepipeline
// http://127.0.0.1:5000/ai/deploy-alert/<AppName>
// http://127.0.0.1:5000/ai/pipeline-alert/<PipelineName>

public class UnifiedGUI extends JFrame {

	private static final long serialVersionUID = 1L;

	JButton fetchDeployments, fetchPipelines, aiDeployAlert, aiPipelineAlert;
	JTextArea output;

	public UnifiedGUI() {
		setTitle("AI + AWS CodeDeploy & CodePipeline");
		setSize(700, 500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);

		fetchDeployments = new JButton("Fetch CodeDeploy");
		fetchPipelines = new JButton("Fetch CodePipeline");
		aiDeployAlert = new JButton("AI: Deploy Alert");
		aiPipelineAlert = new JButton("AI: Pipeline Alert");
		output = new JTextArea();

		fetchDeployments.addActionListener(e -> {
			String json = HttpClientHelper.get("http://127.0.0.1:5000/codedeploy");
			output.setText(json);
		});

		fetchPipelines.addActionListener(e -> {
			String json = HttpClientHelper.get("http://127.0.0.1:5000/codepipeline");
			output.setText(json);
		});

		aiDeployAlert.addActionListener(e -> {
			String app = JOptionPane.showInputDialog("Enter CodeDeploy App Name:");
			if (app != null && !app.isEmpty()) {
				String json = HttpClientHelper.get("http://127.0.0.1:5000/ai/deploy-alert/" + app);
				output.setText(json);
			}
		});

		aiPipelineAlert.addActionListener(e -> {
			String pipeline = JOptionPane.showInputDialog("Enter Pipeline Name:");
			if (pipeline != null && !pipeline.isEmpty()) {
				String json = HttpClientHelper.get("http://127.0.0.1:5000/ai/pipeline-alert/" + pipeline);
				output.setText(json);
			}
		});

		JPanel panel = new JPanel();
		panel.add(fetchDeployments);
		panel.add(fetchPipelines);
		panel.add(aiDeployAlert);
		panel.add(aiPipelineAlert);

		add(panel, "North");
		add(new JScrollPane(output), "Center");

		setVisible(true);
	}

	public static void main(String[] args) {
		new UnifiedGUI();
	}
}
