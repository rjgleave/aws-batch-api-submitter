import json
import logging

import boto3
client = boto3.client(
    service_name='stepfunctions',
    region_name='us-east-1',
    endpoint_url='https://states.us-east-1.amazonaws.com')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    # read dynamo records
    for record in event['Records']:
        
        if record['eventName'] == 'INSERT':
            RunRequest = {
                'runRequestID': record['dynamodb']['NewImage']['runRequestID']['S'],
                'processname': record['dynamodb']['NewImage']['processname']['S'],
                'clientname': record['dynamodb']['NewImage']['clientname']['S'],
                'timestamp': record['dynamodb']['NewImage']['timestamp']['S']
            }

            '''
            response = client.start_execution(
                stateMachineArn='string',
                name='string',
                input='string'
            )
            '''

            # start the state machine
            print "starting the state machine....."
            # build job name
            #job_name = processname + RunRequestID

            # create the base state machine input document
            input_document ={"jobName": "APOST-1","jobDefinition": "arn:aws:batch:us-east-1:99999999999:job-definition/SampleJobDefinition-49e0468e4a867f5:1","jobQueue": "arn:aws:batch:us-east-1:786247309603:job-queue/SampleJobQueue-5da08f800c56cd4", "wait_time": 60}
            # update the jobname and the state machine name
            state_machine_name = "batch-poller-" + RunRequest["processname"] + '-' + RunRequest["clientname"] + '-' + RunRequest["runRequestID"]
            input_document["jobName"]= RunRequest["processname"] + '-' + RunRequest["clientname"] + '-' + RunRequest["runRequestID"]

            print "input document: ", input_document
            print "state machine name: ",state_machine_name

            # start the state machine - passing in the input document and arn
            response = client.start_execution(
                stateMachineArn='arn:aws:states:us-east-1:999999999999:stateMachine:JobStatusPollerStateMachine-Mg9JogmrbUlY',
                name=state_machine_name,
                input= json.dumps(input_document)
            )

            logger.info('RunRequest: ' + json.dumps(RunRequest, indent=2))

            print "Got this record from DynamoDB: ", json.dumps(RunRequest, indent=2)