import boto3
from botocore.exceptions import NoCredentialsError
from uuid import uuid4
import os

IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'images')
SOURCE_BUCKET = 'ImageFileStorage'
s3 = boto3.client('s3')

image_file_count = len(os.listdir(IMAGE_PATH))

for i in range(image_file_count):
    try:
        img_file = 'img_{0}.jpg'.format(str(uuid4()))
        s3.upload_file(IMAGE_PATH, SOURCE_BUCKET,
                       img_file)
        print(f"Upload to S3")
    except FileNotFoundError:
        print(f"The file was not found: {img_file}")
    except NoCredentialsError:
        print("Incorrect credentials")
