import boto3
client = boto3.client('ec2',region_name = "us-east-1")
sns = boto3.client('sns',region_name = "us-east-1")
def lambda_handler(event, context):
    response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Dev',
            ]
        },
    ]
    )
    for instance in response['Reservations']:
        print(instance['Instances'][0]['InstanceId'])
        a = instance['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']

        res = client.create_snapshot(VolumeId = a)
        b = res['SnapshotId']
        c = res['VolumeSize']
        d = "Volume id with '{}' SnapshotId is '{}' and its size '{}'".format(a,b,c)
        res1 = sns.publish(
                TopicArn='arn:aws:sns:us-east-1:156114408639:SNS_ALERTS',
                Message = d,
                Subject='Snapshot Details')
        print(res1)