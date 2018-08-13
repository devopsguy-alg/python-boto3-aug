import boto3
client = boto3.client('sns')
def lambda_handler(event, context):
    a = event['Records'][0]['awsRegion']
    b = event['Records'][0]['eventTime']
    c = event['Records'][0]['s3']['bucket']['name']
    d = event['Records'][0]['s3']['object']['key']
    e = event['Records'][0]['s3']['object']['size']
    f = "In AWS REGION '{}' Created in '{}' In bucket '{}' Object Value '{}' and object size '{}'".format(a,b,c,d,e) 
    res1 = client.publish(
        TopicArn='arn:aws:sns:us-east-1:682447408639:SNS_ALERTS',
        Message = f,
        Subject='S3 Object Details Details')