# upload_to_s3.py
import os
import boto3
from huggingface_hub import snapshot_download

# AWS S3 Configuration
BUCKET_NAME = "your-s3-bucket-name"  # Replace with your actual S3 bucket name
MODEL_ID = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"  # Hugging Face model ID
LOCAL_MODEL_FOLDER = "DeepSeek-R1-Distill-Llama-8B"  # Folder to store the model

# AWS Credentials (Ensure these are set in environment variables for security)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "us-east-1"  # Change as needed

# Initialize S3 client
s3_client = boto3.client("s3", 
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_REGION)

def download_model():
    """Downloads the DeepSeek model from Hugging Face."""
    print("📥 Downloading model from Hugging Face...")
    snapshot_download(repo_id=MODEL_ID, local_dir=LOCAL_MODEL_FOLDER)
    print("✅ Model download complete!")

def upload_directory():
    """Uploads all files from the local model folder to S3."""
    for root, _, files in os.walk(LOCAL_MODEL_FOLDER):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_path, LOCAL_MODEL_FOLDER)
            
            print(f"🚀 Uploading {local_path} → s3://{BUCKET_NAME}/{s3_key}")
            s3_client.upload_file(local_path, BUCKET_NAME, s3_key)
    print("✅ Upload complete! Check your S3 bucket to confirm.")

if __name__ == "__main__":
    download_model()
    upload_directory()
