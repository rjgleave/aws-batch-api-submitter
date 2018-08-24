Submitting AWS Batch Jobs using API Gateway 
==================================================

This solution illustrates how to trigger batch processes from on-premise systems using an http post action to an API.   This is a useful architecture for combining on-premise and cloud processes together into a single workflow.

![Reference Architecture](https://github.com/rjgleave/aws-batch-api-submitter/blob/master/assets/trigger-batch-using-api-gateway.png)

![](https://github.com/rjgleave/aws-batch-api-submitter/blob/master/assets/Trigger-AWS-Batch-Integration-Job-Using-API-Gateway.png)

In this example, an on-premise process runs, followed by a cloud-based process.  At the completion of the on-premise process, an http message is posted to an api, which saves the transaction in DynamoDB.  A trigger on the dynamoDB table invokes a state machine (AWS Step Functions) which submits the job corresponding to the message.  Step Functions will monitor the job for success or failure, until its completion.   


What's Here
-----------

This repo includes:

1. README.md - this file
2. FOLDER: dynamo - this contains code to help build the sample 
transaction table in dynamoDB.  It includes:
    *   schema.json - an example of the dynamoDB schema data structure
    *   read_dynamo_stream.py - the lambda program which reads the dynamodb streams
    *   test_streams.json - a sample stream file for testing the lambda above.
3. FOLDER: api-gateway - contains templates to help build and test the API REST interface
    *   api_gateway_mapping_template.json - this is the mapping document used to create the proxy api for the state machine service.
    *   test_message.json - copy the json document and use to test the API.
4. FOLDER: state_machine  - components to build the state machine
    *   JobStatusPoller.py - a lambda to poll the status of batch jobs.
    *    SubmitJobFunction.py - lambda function to submit a batch job. 
    *   JobStatusPollerStateMachine.json - definition of the state machine
    *   input-template.json - the document used to submit the state machine

Setup Instructions
------------------

1. 



__Additional Resources__

Blog: Using Amazon API Gateway as a proxy for DynamoDB
https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/

SWS Step Functions
https://aws.amazon.com/step-functions/
