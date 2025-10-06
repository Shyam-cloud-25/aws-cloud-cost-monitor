## AWS Cloud Cost Monitor – Setup Guide
This guide explains the step-by-step process for setting up the AWS Cloud Cost Monitor demo project.

## Billing & Budget Setup:
- Go to AWS Billing Dashboard (N. Virginia region).
- Create a new Budget:-
- Period: Monthly
- Amount: $1 (demo)
- Alert Threshold: 20%
- Confirm the budget is created.

## S3 Bucket Setup:
- Create a new S3 bucket in ap-south-1 (Mumbai) region.
- Check bucket overview.

## Lambda Function Setup:
- Create a new Lambda function in Mumbai region.
- Runtime: Python 3.12
- Execution Role: Auto-created (edit later)
- Paste the function code.
- Edit Execution Role in IAM console and attach basic permissions. (CloudWatchFullAccess, S3FullAccess, SNSFullAccess, AWSLambdaBasicExecutionRole)

## SNS Notifications:
- Create a new SNS Topic (Standard).
- Add an Email Subscription.
- Confirm email subscription from inbox.

## CloudWatch Monitoring:
- Lambda pushes custom metric → view in CloudWatch Metrics.
- Create a CloudWatch Alarm on the metric.
- Alarm state will show as OK / ALARM / Insufficient Data.

## End-to-End Test:
- Go back to Budget Notifications and ensure SNS topic is linked.
- Trigger the test alert.
- Check your email inbox for the final notification.

## ✅ Project Completed

- At this point, the AWS Cloud Cost Monitor demo project is complete!
We have a working cost monitoring system that:
 - Tracks budget usage.
 - Sends alerts via SNS.
 - Uses Lambda & CloudWatch for monitoring.