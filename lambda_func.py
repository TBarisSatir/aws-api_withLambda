import json

def lambda_handler(event, context):
    try:
        # Sabit mesaj
        message = "Hello from AWS Lambda! @baris"

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"Status Code" : "200", " Message": message})
        }

    except KeyError as e:
        return {
            "statusCode": 404,
            "body": json.dumps({"error 404": f"Key not found: {str(e)}"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error 500": f"Internal server error: {str(e)}"})
        }
