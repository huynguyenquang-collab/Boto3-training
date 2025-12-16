import boto3
import os

#create bucket upload start_instance.py and terminate_instance.py to S3
def upload_file_to_s3(file_name, bucket_name, object_name=None, region='ap-southeast-2'):
    
    #create s3 bucket if not exists
    s3 = boto3.resource('s3', region_name=region)
    if s3.Bucket(bucket_name) not in s3.buckets.all():
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket {bucket_name} created.")

    # Create S3 client
    s3_client = boto3.client('s3', region_name=region)
    
    # Ensure object_name (S3 Key) is a string. Default to the file's basename when None.
    if object_name is None:
        object_name = os.path.basename(file_name)

    if not isinstance(object_name, str):
        object_name = str(object_name)

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to bucket {bucket_name} as {object_name}.")
        return True
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return False

if __name__ == "__main__":
    bucket_name = "huy-intern-bucket" 
    
    # Upload start_instance.py
    upload_file_to_s3('./start_instance.py',bucket_name)
    
    # Upload terminate_instance.py
    upload_file_to_s3('./terminate_instance.py', bucket_name)
