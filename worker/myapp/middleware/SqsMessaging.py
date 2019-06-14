import boto3

def SendMessage(queue_name, respondent):
    sqs = boto3.resource('sqs', region_name='us-east-1')
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    queue.send_message(MessageBody=respondent)
    #sqs.send_message(QueueUrl = queue_url, DelaySeconds=0, MessageBody = respondent)

