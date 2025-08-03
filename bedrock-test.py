import boto3
import json
from botocore.exceptions import ClientError

# Set the AWS Region
region = "ap-southeast-2"

# Initialize the Bedrock Runtime client
client = boto3.client("bedrock-runtime", region_name=region)

model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

prompt = """Please analyze a GitHub repository with the following criteria:
- Architecture
- Code complexity
- Testing practices

Context:
- The repository is a Node.js REST API.
- GitHub repository URL: https://github.com/lethaldose/summary-stats

Objectives:
- I want to enhance the codebase and add new endpoints for additional functionality.
- I will provide specific requirements for the new functionality.

Questions:
1. Based on the provided requirements, how much time would it take to implement the new functionality, including the necessary testing effort?
2. Please break down the estimate into development and testing phases.
3. If possible, suggest ways to improve the architecture or testing approach.

Please provide your analysis in a clear, structured format.

I want to enhance the `stats-summary` API to include the count of employees for each group in the summary response. Please describe the changes needed in the codebase, estimate the effort required, and update the response structure example to include the new `count` field for each group. 
Additionally, provide separate effort estimates for how much time a senior engineer and a mid-level engineer would take to complete this task."""

inference_parameters = {
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 4000,
    "temperature": 0.5,
    "anthropic_version": "bedrock-2023-05-31",
}


request_payload = json.dumps(inference_parameters)

try:
    response = client.invoke_model(
        modelId=model_id,
        body=request_payload,
        contentType="application/json",
        accept="application/json",
    )

    response_body = json.loads(response["body"].read())
    generated_text = response_body["content"][0]["text"]
    print("Generated Text:\n", generated_text)

except ClientError as e:
    print(f"ClientError: {e.response['Error']['Message']}")
except Exception as e:
    print(f"An error occurred: {e}")
