
# 🚀 DeepSeek Self-Hosting on AWS  

This project enables you to **self-host DeepSeek** securely on AWS using S3 and Amazon Bedrock.  

## **🔧 Setup & Deployment**  

1️⃣ **Clone the repository**  

git clone https://github.com/your-username/DeepSeek-Self-Hosting.git  
cd DeepSeek-Self-Hosting

2️⃣ Install dependencies

pip install boto3

3️⃣ Upload model files to S3

python upload_to_s3.py

4️⃣ Automate deployment with GitHub Actions

Add your AWS credentials as GitHub Secrets (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY).

Push changes to main, and the workflow will trigger automatically.

🔗 Try It Yourself!

