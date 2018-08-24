import json
import boto3

print('Loading function')

batch = boto3.client('batch')

def lambda_handler(event, context):
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))
    # Get jobId from the event
    jobId = event['jobId']

    try:
        # Call DescribeJobs
        response = batch.describe_jobs(jobs=[jobId])
        # Log response from AWS Batch
        print("Response: " + json.dumps(response, indent=2))
        # Return the jobtatus
        jobStatus = response['jobs'][0]['status']
        return jobStatus
    except Exception as e:
        print(e)
        message = 'Error getting Batch Job status'
        print(message)
        raise Exception(message)