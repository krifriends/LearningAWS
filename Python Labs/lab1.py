import boto3
import json
# Using Client
# my_client =boto3.client('s3')
my_client=boto3.resource('s3','us-east-1').meta.client
bucket_name = 'my-new-bucket-lab1-upd'
my_client.create_bucket(Bucket=bucket_name)
response = my_client.put_bucket_versioning(
    Bucket=bucket_name,   
    VersioningConfiguration={
        'MFADelete': 'Disabled',
        'Status': 'Enabled'
    }
)
print(response)
bucket_policy = {
    "Version": "2008-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::my-new-bucket-lab1-upd/*",
                "arn:aws:s3:::my-new-bucket-lab1-upd"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": [
                        "98.235.158.1/32"
                    ]
                }
            }
        },
        {
            "Sid": "DenyOneObjectIfRequestNotSigned",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-new-bucket-lab1-upd/report.html",
            "Condition": {
                "StringNotEquals": {
                    "s3:authtype": "REST-QUERY-STRING"
                }
            }
        }
    ]
}

# # Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# # Set the new policy
my_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

backdrop_camera ='backdrop_camera.jpg'
my_client.upload_file(backdrop_camera, bucket_name, backdrop_camera)

callback_html = 'callback.html'
my_client.upload_file(callback_html, bucket_name, callback_html)

config_js = 'config.js'
my_client.upload_file(config_js, bucket_name, config_js)

core_css='core.css'
my_client.upload_file(core_css, bucket_name, core_css)

flex_search_js='flex_search.js'
my_client.upload_file(flex_search_js, bucket_name, flex_search_js)

index_html='index.html'
my_client.upload_file(index_html, bucket_name, index_html)

jquery_js ='jquery.js'
my_client.upload_file(jquery_js, bucket_name, jquery_js)

kiosk_png ='kiosk.png'
my_client.upload_file(kiosk_png, bucket_name, kiosk_png)

kiosk_bottom_png='kiosk_bottom.png'
my_client.upload_file(kiosk_bottom_png, bucket_name, kiosk_bottom_png)

kiosk_left_png='kiosk_left.png'
my_client.upload_file(kiosk_left_png, bucket_name, kiosk_left_png)

kiosk_right_png='kiosk_right.png'
my_client.upload_file(kiosk_right_png,bucket_name,kiosk_right_png)

kiosk_top_png='kiosk_top.png'
my_client.upload_file(kiosk_top_png,bucket_name,kiosk_top_png)

main_css='main.css'
my_client.upload_file(main_css,bucket_name,main_css)

main_js ='main.js'
my_client.upload_file(main_js,bucket_name,main_js)

products_js='products.js'
my_client.upload_file(products_js,bucket_name,products_js)

report_html='report.html'
my_client.upload_file(report_html,bucket_name,report_html)

reset_css='reset.css'
my_client.upload_file(reset_css,bucket_name,reset_css)

search_css ='search.css'
my_client.upload_file(search_css,bucket_name,search_css)

search_js='search.js'
my_client.upload_file(search_js,bucket_name,search_js)

response2 = my_client.list_objects(Bucket=bucket_name)
# print(response2)
for content in response2['Contents']:
    obj_dict = my_client.get_object(Bucket=bucket_name, Key=content['Key'])
    print(content['Key'],obj_dict['LastModified'])