import boto3

# Using Client
my_client =boto3.client('s3')
# my_client.create_bucket(Bucket='demo-krishna-bucket')
# response = my_client.put_bucket_versioning(
#     Bucket='demo-krishna-bucket',   
#     VersioningConfiguration={
#         'MFADelete': 'Disabled',
#         'Status': 'Enabled'
#     }
# )
# print(response)

fileName ='dog3.jpg'
bucket_name ='demo-krishna-bucket'
# my_client.upload_file(fileName, bucket_name, fileName)

response2 = my_client.list_objects(Bucket='demo-krishna-bucket')
# print(response2)
for content in response2['Contents']:
    obj_dict = my_client.get_object(Bucket='demo-krishna-bucket', Key=content['Key'])
    print(content['Key'],obj_dict['LastModified'])


#using resource
s3 = boto3.resource('s3')
bucket = s3.Bucket('demo-krishna-bucket')
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)

#using resource with client
s3_client = boto3.resource('s3').meta.client
# print( s3_client.list_objects(Bucket='demo-krishna-bucket'))
for s3_response in  s3_client.list_objects(Bucket='demo-krishna-bucket')['Contents']:
    new_obj = s3_client.get_object(Bucket='demo-krishna-bucket', Key= s3_response['Key'])
    print(s3_response['Key'],new_obj['LastModified'])


# mydragondata   
my_dragon_client =boto3.client('s3')
my_dragon_client.create_bucket(Bucket='mydragondata')
my_dragon_response = my_dragon_client.put_bucket_versioning(
    Bucket='mydragondata',   
    VersioningConfiguration={
        'MFADelete': 'Disabled',
        'Status': 'Enabled'
    }
)
print(my_dragon_response)
dragonfileName ='DragonData.json'
dragon_bucket_name ='mydragondata'
my_dragon_client.upload_file(dragonfileName, dragon_bucket_name, dragonfileName)
