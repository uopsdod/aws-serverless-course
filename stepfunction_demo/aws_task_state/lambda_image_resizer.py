import json
import boto3
from PIL import Image
from io import BytesIO

s3_client = boto3.client('s3')

def resize_image(image_data, size):
    image = Image.open(BytesIO(image_data))
    image = image.resize(size, Image.LANCZOS)
    
    # Convert image to RGB if it's RGBA
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    output = BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    return output

def lambda_handler(event, context):
    print('event: ', event)
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # object_key = event['Records'][0]['s3']['object']['key']
    bucket_name = event['bucket_name']
    object_key = event['object_key']
    image_size_target = event['taskoutput']['image_size_target'] # use taskoutput because of step function requirement
    
    filename = object_key.split('.')[0]
    extension = object_key.split('.')[1]

    # Download the image from S3
    s3_response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    image_data = s3_response['Body'].read()

    # Define the sizes and new keys
    sizes = [(image_size_target, image_size_target)]
    resized_keys = [
        f"resized/{filename}_{image_size_target}x{image_size_target}.{extension}",
    ]

    # Resize and upload the images
    for size, new_key in zip(sizes, resized_keys):
        resized_image = resize_image(image_data, size)
        s3_client.upload_fileobj(resized_image, bucket_name, new_key, ExtraArgs={'ContentType': 'image/jpeg'})

    return {
        'statusCode': 200,
        'body': json.dumps(f'Images resized as {image_size_target}x{image_size_target} and uploaded successfully!')
    }
