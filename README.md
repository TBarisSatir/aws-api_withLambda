# AWS Lambda + API Gateway "Hello World" API

A simple serverless API that returns a JSON response via AWS Lambda and API Gateway.

## Overview
This project demonstrates a minimal AWS serverless setup:

- **AWS Lambda** runs a small Python function.
- **API Gateway** exposes it via a public HTTP endpoint.

## Getting Started

Follow these steps to create your own endpoint in your AWS account:

1. **Deploy the Lambda function**  
   - You can use Terraform (`main.tf`) or deploy manually via AWS Console.
2. **Deploy API Gateway** and integrate it with the Lambda function.
3. **Access your own endpoint**  

GET https://<your-api-id>.execute-api.<your-region>.amazonaws.com/hello

Replace `<your-api-id>` and `<your-region>` with values from your AWS account.

> **Note:** Do not share your endpoint publicly to avoid unexpected AWS charges.

## Example Response

```json
{
"message": "Hello from AWS Lambda! @baris"
}
