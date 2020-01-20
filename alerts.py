import boto3
ec2= boto3.client('ec2',region_name= 'us-east-1')
sns = boto3.client('sns',region_name= 'us-east-1')
#ec2 = boto3.client('ec2',region_name= 'us-east-1')
response = ec2.describe_instances()
for x in response['Reservations']:
    a = x['Instances'][0]['ImageId']
    b = x['Instances'][0]['InstanceId']
    c = x['Instances'][0]['InstanceType']
    for y in x['Instances']:
        for z in y['Tags']:
            q = z['Value']
        e = y['State']['Name']
        # print("Instance with instance id is {}, Instance type is {}, name is {} , and its state is {}".format(b,c,q,e))
        # print(b)
        res = ec2.stop_instances(
            InstanceIds=[b])
        # print(res)
        for p in res['StoppingInstances']:
            s = p['CurrentState']['Name']
            s1 =  p['InstanceId']
            s2 = p['PreviousState']['Name']
            s4 = ("Instance id with '{}', Previous state is '{}' and current state is '{}'".format(s1,s2,s))
res1 = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:5654647408639:SNS_ALERTS',
    Message=s4,
    Subject='EC2sTOPaLERTS')
