Submitting AWS Batch Jobs using API Gateway 
==================================================

This solution illustrates how to trigger batch processes from on-premise systems using an http post action to an API.   This is a useful architecture for combining on-premise and cloud processes together into a single workflow.

![Reference Architecture](https://github.com/rjgleave/aws-batch-api-submitter/blob/master/assets/trigger-batch-using-api-gateway.png)

In this example, an on-premise process runs, followed by a cloud-based process.  At the completion of the on-premise process, an http message is posted to an api, which saves the transaction in DynamoDB.  A trigger on the dynamoDB table invokes a state machine (AWS Step Functions) which submits the job corresponding to the message.  Step Functions will monitor the job for success or failure, until its completion.   

What's Here
-----------

This repo includes:

1. README.md - this file
2. FOLDER: dynamo - this contains code to help build the tag group table in dynamoDB.  It includes:
    *   createTagGroupTable.py - a program to create the base dynamo table
    *   DataEntryTemplate.xlsx - an Excel template with sample data for the dynamo table
    *   sample-data.csv - a CSV extract of the excel file above
    *   sample-data.json - a JSON equivalent to the CSV file above
    *   loadTagGroupTable.py - a program to load the dynamodb table with sample data
3. FOLDER: policy - contains a json file for defining a custom policy:  custom-tag-group-policy.json
4. FOLDER: tag-builder-direct  - It includes:
    *   tagbuilder.py - the main lambda program to update resources with tags.  
5. FOLDER: tag-builder-lambda - It includes:
    *   tagbuilder-paginate.py - same as lambda program above, except can be called from command line.
6. FOLDER: api-throttler - contains the lambda which is triggered by SQS.  This performs the call to the AWS ResourceGroupsAPI to update tags if you are operating in de-coupled mode (see the SQS-ENABLED environment variable below)

Setup Instructions
------------------

1. 



__Additional Resources__

SWS Step Functions
https://aws.amazon.com/step-functions/
