import boto3
import json
from botocore.exceptions import ClientError

# Set the AWS Region
region = "ap-southeast-2"

# Initialize the Bedrock Runtime client
client = boto3.client("bedrock-runtime", region_name=region)

# Define the model ID for Claude 3 Haiku
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Define the input prompt
prompt = "Command: Compose an email from Tom, Customer Service Manager, to the customer 'Nancy' who provided negative feedback on the service provided by our customer support engineer"

# Configure inference parameters for Claude Messages API
inference_parameters = {
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 512,
    "temperature": 0.5,
    "anthropic_version": "bedrock-2023-05-31",
}

# Convert the request payload to JSON
request_payload = json.dumps(inference_parameters)

try:
    # Invoke the model
    response = client.invoke_model(
        modelId=model_id,
        body=request_payload,
        contentType="application/json",
        accept="application/json",
    )

    # Decode the response body
    response_body = json.loads(response["body"].read())

    # Extract and print the generated text
    generated_text = response_body["content"][0]["text"]
    print("Generated Text:\n", generated_text)

except ClientError as e:
    print(f"ClientError: {e.response['Error']['Message']}")
except Exception as e:
    print(f"An error occurred: {e}")
