a = {
  'Records': [
    {
      'eventVersion': '2.0',
      'eventSource': 'aws:s3',
      'awsRegion': 'us-east-1',
      'eventTime': '2018-08-11T17:18:01.885Z',
      'eventName': 'ObjectCreated:Put',
      'userIdentity': {
        'principalId': 'A34TOS99FY3UNY'
      },
      'requestParameters': {
        'sourceIPAddress': '116.75.87.200'
      },
      'responseElements': {
        'x-amz-request-id': '0D4FE9DA7B8D65A9',
        'x-amz-id-2': 'eENJsuCcdoaWuEaR9nrPxFYeyb4rTZDBD6s/jYlRjhubbSmVJr3IcVSRt7mQqmsduv2BhzTyf+k='
      },
      's3': {
        's3SchemaVersion': '1.0',
        'configurationId': '49ad3caf-85fb-4fb2-ad8a-d6bc5690d7b6',
        'bucket': {
          'name': 'mptechno-suresh',
          'ownerIdentity': {
            'principalId': 'A34TOS99FY3UNY'
          },
          'arn': 'arn:aws:s3:::mptechno-suresh'
        },
        'object': {
          'key': 'jenkins-and-perfecto.png',
          'size': 115229,
          'eTag': '2ce15b4cfd92c57705a4cfea4ec512bb',
          'sequencer': '005B6F1A49D34540D5'
        }
      }
    }
  ]
}
b = a['Records'][0]['bucket']['name']
print(b)