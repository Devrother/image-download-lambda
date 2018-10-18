import urllib.request
import boto3
import json

# Let's use Amazon S3
s3 = boto3.resource('s3')

def download_image(event, context):
    message = event['Records'][0]['messageAttributes']['logo_thumb_img_url']['stringValue']
    filename = event['Records'][0]['messageAttributes']['filename']['stringValue']
    form = ".jpg"
    data = urllib.request.urlopen(message).read()
    s3.Bucket('onsuk-bucket').put_object(Key=str(filename) + form, Body=data)