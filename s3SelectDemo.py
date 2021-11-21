import boto3

s3=boto3.resource('s3','us-east-1').meta.client
ssm = boto3.client('ssm','us-east-1')

bucket_name = ssm.get_parameter(
    Name='dragon_data_bucket_name',
    WithDecryption=False
)['Parameter']['Value']

file_name = ssm.get_parameter(
    Name='dragon_data_file_name',
    WithDecryption=False
)['Parameter']['Value']

print('the bucket name is ',bucket_name)
print('the json file name is ', file_name)


def listDragons():
    expression = "SELECT * FROM s3object s"
    #fetching results in CSV
    # result = s3.select_object_content(
    #         Bucket=bucket_name,
    #         Key=file_name,
    #         ExpressionType='SQL',
    #         Expression=expression,
    #         InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
    #         OutputSerialization = {'CSV': {}}
    # )

    #fetching results in JSON
    result = s3.select_object_content(
            Bucket=bucket_name,
            Key=file_name,
            ExpressionType='SQL',
            Expression=expression,
            InputSerialization = {'JSON': {"Type": "Document"}},
            OutputSerialization = {'JSON': {}}
    )
    for event in result['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
            print(statsDetails['BytesProcessed'])
            print("Stats details bytesReturned: ")
            print(statsDetails['BytesReturned'])

listDragons()