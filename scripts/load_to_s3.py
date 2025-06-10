import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')

    try:
        print("⏳ Uploading to S3...")
        print(f"File: {file_name}")
        print(f"Bucket: {bucket}")
        print(f"Object Name: {object_name}")
        
        s3.upload_file(file_name, bucket, object_name)

        print(f"✅ File '{file_name}' uploaded to S3 bucket '{bucket}' as '{object_name}'")
    except FileNotFoundError:
        print("❌ The file was not found.")
    except NoCredentialsError:
        print("❌ Credentials not available.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    upload_to_s3(
        file_name="data/transformed_youtube.csv",
        bucket="youtube-etl-oladapo",  # ✅ Replace with your actual bucket name
        object_name="youtube/transformed_youtube.csv"
    )
