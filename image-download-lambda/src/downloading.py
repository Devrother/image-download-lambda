import urllib.request
import random
import boto3

image_url_list = ['https://static.wanted.co.kr/images/wdes/12553_1_0.46dea2f9.png',
              'https://static.wanted.co.kr/images/wdes/6789_1_0.78ddb2f9.jpg',
              'https://static.wanted.co.kr/images/wdes/9335_1_0.54619b4c.jpg',
              'https://static.wanted.co.kr/images/wdes/4179_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/4337_1_0.295e2c29.jpg',
              'https://static.wanted.co.kr/images/wdes/8473_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/8474_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/5057_1_0.b42355e8.jpg',
              'https://static.wanted.co.kr/images/wdes/6053_1_0.875eb75c.jpg',
              'https://static.wanted.co.kr/images/wdes/8918_1_0.70cc3e73.jpg',
              'https://static.wanted.co.kr/images/wdes/8151_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/14336_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/11282_1_0.53ae1b34.jpg',
              'https://static.wanted.co.kr/images/wdes/12302_1_0.8bb354d8.jpg',
              'https://static.wanted.co.kr/images/wdes/12483_1_0.a7fe21bd.jpg',
              'https://static.wanted.co.kr/images/wdes/8475_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/6498_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/10612_1_0.fdfd51d9.jpg',
              'https://static.wanted.co.kr/images/wdes/14344_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/8408_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/14346_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/3561_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/8360_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/10569_1_0.e323e3b1.jpg',
              'https://static.wanted.co.kr/images/wdes/10012_1_0.c34ca64d.jpg',
              'https://static.wanted.co.kr/images/wdes/10466_1_0.751abb16.jpg',
              'https://static.wanted.co.kr/images/wdes/2145_1_0.8c56a855.jpg',
              'https://static.wanted.co.kr/images/wdes/14505_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/4196_1_0.d3b44a16.jpg',
              'https://static.wanted.co.kr/images/wdes/12602_1_0.d41c1e98.jpg',
              'https://static.wanted.co.kr/images/wdes/3946_1_0.133a5295.jpg',
              'https://static.wanted.co.kr/images/wdes/12584_1_0.94823b7b.jpg',
              'https://static.wanted.co.kr/images/wdes/8150_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/10357_1_0.06564bb4.jpg',
              'https://static.wanted.co.kr/images/wdes/12481_1_0.e2fc94c7.jpg',
              'https://static.wanted.co.kr/images/wdes/8146_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/12691_1_0.f8bd940f.jpg',
              'https://static.wanted.co.kr/images/wdes/14221_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/2449_1_0.9d4790ce.jpg',
              'https://static.wanted.co.kr/images/wdes/8148_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/12054_1_0.12d2838f.jpg',
              'https://static.wanted.co.kr/images/wdes/14324_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/8152_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/3240_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/4236_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/12586_1_0.6e025214.jpg',
              'https://static.wanted.co.kr/images/wdes/14268_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/5958_1_0.jpg',
              'https://static.wanted.co.kr/images/wdes/5855_1_0.jpg']


s3 = boto3.resource('s3')

# image_url_list_test = ['https://static.wanted.co.kr/images/wdes/12553_1_0.46dea2f9.png', 'https://static.wanted.co.kr/images/wdes/6789_1_0.78ddb2f9.jpg']

def download_image(event, context):
    for url in image_url_list:
        filename = random.randrange(1, 1000)
        form = ".jpg"
        data = urllib.request.urlopen(url).read()
        s3.Bucket('onsuk-bucket').put_object(Key=str(filename) + form, Body=data)

# for url in image_url_list:
#         filename = random.randrange(1, 1000)
#         form = ".jpg"
#         data = urllib.request.urlopen(url).read()
#         s3.Bucket('onsuk-bucket').put_object(Key=str(filename) + form, Body=data)