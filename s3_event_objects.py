def lambda_handler(event, context):
    print(str(event))
    a = event
    b = a['Records'][0]['s3']['bucket']['name']
    c = a['Records'][0]['s3']['object']['key']
    d = a['Records'][0]['s3']['object']['size']
    e = a['Records'][0]['awsRegion']
    print("in region '{}' in the Bucket '{}' recently file '{}' is uploaded with size '{}'".format(e,b,c,d))