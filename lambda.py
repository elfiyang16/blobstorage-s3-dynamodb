
import boto3
from PIL import Image
from PIL.ExifTags import TAGS
from uuid import uuid4

TABLE_NAME = "ImgMeta"
tag_obj = {}
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
ddb = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    path = '/tmp/{}'.format(key)

    with open(path, 'wb') as img_file:
        s3_client.download_fileobj(source_bucket, key, img_file)

    image = Image.open(path)
    exif = image.getexif()
    tag_obj['image_id'] = str(uuid4())
    for tag_id in exif:
        tag = TAGS.get(tag_id, tag_id)
        data = exif.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        tag_obj[tag] = str(data)
        print(f"{tag}: {data}")

    response = ddb.put_item(Item=tag_obj)
    print(response)
