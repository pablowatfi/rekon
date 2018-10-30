import boto3
import base64

photo_path = '/Users/pablowatfi/Desktop/AllHands.png'

with open(photo_path, "rb") as image_file:
    # encoded_photo = base64.b64encode(image_file.read())
    encoded_photo = image_file.read()

# encoded_photo = open(photo_path, 'rb')

client = boto3.client('rekognition')

response = client.detect_faces(
    Image={
        'Bytes': encoded_photo,
    },
    Attributes=[
        'DEFAULT',
        'ALL',
    ]
)

print(response)
males =0
females = 0

for face_det in response['FaceDetails']:
    if face_det['Gender']['Value'] == 'Male':
        males += 1
    if face_det['Gender']['Value'] == 'Female':
        females += 1

print(f'We found {males} males and {females} females in the picture.')
