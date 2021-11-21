import boto3

my_client =boto3.client('s3')
my_client.create_bucket(Bucket='demo-krishna-bucket')
# response = client.list_objects(Bucket=')

