package com.ai.aws.codedeploy.codepipeline.utility;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpClientHelper {
	
	public static String get(String endpoint) {
		
		try {
			URL url = new URL(endpoint);
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setRequestMethod("GET");

			BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
			StringBuilder content = new StringBuilder();
			String line;
			while ((line = in.readLine()) != null) {
				content.append(line).append("\n");
			}
			in.close();
			con.disconnect();
			return content.toString();
		} catch (Exception e) {
			return "Error: " + e.getMessage();
		}
	}
}