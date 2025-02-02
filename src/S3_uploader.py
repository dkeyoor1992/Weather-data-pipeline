from src.config import AWS_CONFIG
import boto3
from io import StringIO

class S3Uploader:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_CONFIG[""],
            aws_secret_access_key=AWS_CONFIG[""]
        )
        self.bucket_name = AWS_CONFIG["s3_bucket_name"]

    def upload_df_to_s3(self, df):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        self.s3_client.put_object(Bucket=self.bucket_name, Key=AWS_CONFIG["s3_file_name"], Body=csv_buffer.getvalue())
        print(f"File uploaded to s3://{self.bucket_name}/{AWS_CONFIG['s3_file_name']}")
