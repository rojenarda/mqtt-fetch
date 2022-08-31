import json
import boto3

def lambda_handler(event, context):

    try:
        table = boto3.resource("dynamodb").Table("mqtt_message")
        table.put_item(Item=event)

    except Exception as e:
        return {
        "statusCode": 500,
        "message": str(e).replace("\\", "")
    }

    return {
        "statusCode": 200,
        "message": "done"
    }