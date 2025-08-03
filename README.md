# Amazon Bedrock Python Examples

This repository contains Python examples for interacting with Amazon Bedrock foundation models, specifically focusing on Claude models for code analysis and repository assessment.

## Overview

The project demonstrates how to use AWS Bedrock to analyze GitHub repositories and provide comprehensive assessments including:

- Architecture analysis
- Code complexity evaluation
- Testing practices review
- Enhancement recommendations
- Time estimates for development tasks

## Files

- `bedrock-c3.7.py` - Example script using Claude 3.7 Sonnet
- `bedrock-test.py` - Example script using Claude 3.5 Sonnet
- `titan.py` - Example script using Claude 3 Haiku

## Prerequisites

1. **AWS Account**: You need an AWS account with access to Amazon Bedrock
2. **AWS CLI**: Install and configure AWS CLI
3. **Python**: Python 3.7 or higher
4. **Dependencies**: Install required Python packages

## Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install boto3
```

### 2. Configure AWS Credentials

```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=ap-southeast-2
```

### 3. Bedrock Access

Ensure your AWS account has access to Amazon Bedrock and the required models. You may need to:

- Request access to specific models in the AWS Bedrock console
- Set up inference profiles for models that require them

## Usage

### Running the Scripts

```bash
# Activate virtual environment
source venv/bin/activate

# Run Claude 3.7 example
python bedrock-c3.7.py

# Run Claude 3.5 example
python bedrock-test.py

# Run Claude 3 Haiku example
python titan.py
```

### Model Configuration

The scripts are configured to use different Claude models:

- **Claude 3.7 Sonnet**: `apac.anthropic.claude-3-7-sonnet-20250219-v1:0`
- **Claude 3.5 Sonnet**: `anthropic.claude-3-5-sonnet-20241022-v2:0`
- **Claude 3 Haiku**: `anthropic.claude-3-haiku-20240307-v1:0`
- **Claude 4 Sonnet**: `apac.anthropic.claude-sonnet-4-20250514-v1:0`

### Customizing the Analysis

You can modify the prompt in any script to analyze different repositories or ask different questions:

```python
prompt = """Your custom analysis request here"""
```

## Example Output

The scripts provide comprehensive analysis including:

- **Architecture Assessment**: Framework analysis, code structure, design patterns
- **Complexity Evaluation**: Code quality, maintainability, technical debt
- **Testing Review**: Test coverage, testing strategies, improvement suggestions
- **Enhancement Planning**: Detailed implementation guidance with code examples
- **Time Estimates**: Development time estimates for senior and mid-level engineers

## AWS Region Configuration

The scripts are configured for the `ap-southeast-2` region. To use a different region:

```python
region = "your-preferred-region"
```

## Error Handling

The scripts include error handling for:

- Invalid model identifiers
- AWS authentication issues
- Network connectivity problems
- Bedrock service errors

## Troubleshooting

### Common Issues

1. **"The provided model identifier is invalid"**

   - Check if the model is available in your region
   - Verify the model ID is correct
   - Ensure you have access to the model

2. **"Invocation of model ID with on-demand throughput isn't supported"**

   - Use the inference profile instead of direct model ID
   - Check available inference profiles: `aws bedrock list-inference-profiles`

3. **Authentication errors**
   - Verify AWS credentials are properly configured
   - Check IAM permissions for Bedrock access

### Getting Help

- Check AWS Bedrock documentation
- Verify model availability in your region
- Ensure proper IAM permissions are set up

## Contributing

Feel free to contribute by:

- Adding new model examples
- Improving error handling
- Enhancing the analysis prompts
- Adding more comprehensive documentation

## License

This project is for educational and demonstration purposes. Please ensure compliance with AWS Bedrock terms of service and usage policies.
