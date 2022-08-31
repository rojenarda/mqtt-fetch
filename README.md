AWS SAM Application that creates a DynamoDB table with primary keys "name" and "surname",
and sets a Lambda function that triggers when an MQTT message is received under the topics "sam/#".
Messages should be in JSON format, Lambda function adds the message content to the DynamoDB table.