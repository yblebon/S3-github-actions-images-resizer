import boto3
import os
import sys

s3_client = boto3.client('s3',
	endpoint_url=os.getenv("AWS_ENDPOINT"),
	aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
	aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

input_dir = sys.argv[1]
upload_dir = sys.argv[2]
print(f"Uploader input directory: {input_dir}")
print(f"Uploader upload directory: {upload_dir}")

for fname in os.listdir(input_dir):
  fpath = os.path.join(input_dir, fname)
  s3_client.upload_file(fpath,os.getenv("AWS_BUCKET_NAME", "bucket-test"), f"{upload_dir}/{fname}")
