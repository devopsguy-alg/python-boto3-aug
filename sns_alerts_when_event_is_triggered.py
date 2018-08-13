import boto3
sns = boto3.client("sns")
def lambda_handler(event, context):
    a = event['account']
    b = event['region']
    c = event['detail']['instance-id']
    p = event['detail']['state']
    q = ("In region '{}' Instance id with '{}' its stste is '{}'".format(b,c,p))
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:755967408639:SNS_ALERTS',
        Message=q,
        Subject='MyAlerts')