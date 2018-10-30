

#  Bytes
# Blob of image bytes up to 5 MBs.
#
# Type: Base64-encoded binary data object
#
# Length Constraints: Minimum length of 1. Maximum length of 5242880.
#
# Required: No
#
# S3Object
# Identifies an S3 object as the image source.
#
# Type: S3Object object

# Required: No

# OTHER PARAMS
# Image
# The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
#
# Type: Image object
#
# Required: Yes
#
# MaxLabels
# Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels.
#
# Type: Integer
#
# Valid Range: Minimum value of 0.
#
# Required: No
#
# MinConfidence
# Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.
#
# If MinConfidence is not specified, the operation returns labels with a confidence values greater than or equal to 50 percent.
#
# Type: Float
#
# Valid Range: Minimum value of 0. Maximum value of 100.
#
# Required: No

request_sample = {
   "Image": {
      "Bytes": blob,
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "MaxLabels": number,
   "MinConfidence": number
}