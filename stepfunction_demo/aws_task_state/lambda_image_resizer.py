import json
import boto3
from PIL import Image
from io import BytesIO

s3_client = boto3.client('s3')

def resize_image(image_data, size):
    image = Image.open(BytesIO(image_data))
    image = image.resize(size, Image.ANTIALIAS)
    output = BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    return output

def lambda_handler(event, context):
    print('event: ', event)
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # object_key = event['Records'][0]['s3']['object']['key']
    bucket_name = 'XXXXX'
    object_key = 'XXXXX'

    # Download the image from S3
    s3_response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    image_data = s3_response['Body'].read()

    # Define the sizes and new keys
    sizes = [(300, 300), (500, 500), (700, 700)]
    resized_keys = [
        f"resized/300x300/{object_key}",
        f"resized/500x500/{object_key}",
        f"resized/700x700/{object_key}",
    ]

    # Resize and upload the images
    for size, new_key in zip(sizes, resized_keys):
        resized_image = resize_image(image_data, size)
        s3_client.upload_fileobj(resized_image, bucket_name, new_key, ExtraArgs={'ContentType': 'image/jpeg'})

    return {
        'statusCode': 200,
        'body': json.dumps('Images resized and uploaded successfully!')
    }
