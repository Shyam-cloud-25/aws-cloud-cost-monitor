## AWS Cloud Cost Monitor (Demo Project)

📌 Overview:
- This project demonstrates how to set up a simple cloud cost monitoring system on AWS.
- It uses AWS Budgets, CloudWatch, SNS, S3, and Lambda to track usage and send alerts when spending crosses a defined threshold.
- The project is designed as a demo to showcase skills in AWS services and cloud cost management.

## 🏗️ Architecture

The solution works as follows:
- AWS Budget → Tracks costs and defines threshold.
- SNS (Simple Notification Service) → Sends alerts via email.
- Lambda → Processes budget alerts and pushes custom metrics to CloudWatch.
- CloudWatch → Monitors custom metrics and triggers alarms.
- S3 → Acts as backend storage for logs or future extension.

## ⚙️ Services Used:
- AWS Budgets – To define cost limits and thresholds.
- Amazon SNS – For sending email notifications.
- AWS Lambda – Serverless function to handle budget alerts.
- Amazon CloudWatch – For monitoring metrics and alarms.
- Amazon S3 – Storage for logs or demo backend.

## 🚀 Project Setup (Demo Steps):
- Created a budget with threshold = 20% of $1.
- Set up an S3 bucket in ap-south-1 (Mumbai) region.
- Deployed a Lambda function with Python to process alerts.
- Configured IAM role for Lambda execution.
- Created SNS topic & email subscription for notifications.
- Connected Budget notifications → SNS → Lambda → CloudWatch.
- Verified end-to-end by receiving test email alerts.

## 📸 Screenshots:

Screenshots for each step are available in the /screenshots folder, covering:
- Budget creation
- S3 setup
- Lambda code & permissions
- SNS topic & subscription
- CloudWatch metric & alarm

## Final alert email:

🎯 Key Learning:
- How to integrate AWS Budgets with CloudWatch and SNS.
- How to use Lambda for monitoring automation.
- Best practices for keeping AWS costs under control.

## Remember to Cleanup all the Services. 