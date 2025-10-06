import boto3
import json
import random
from datetime import datetime

s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

#  bucket name and SNS ARN
BUCKET_NAME = "cost-calculator-demo-shyam"
SNS_TOPIC_ARN = "CostAlert"

def lambda_handler(event, context):
    # Generate a random demo cost between 0.1 and 1.0
    demo_cost = round(random.uniform(0.1, 1.0), 2)

    # 1. Save to S3 as JSON
    report = {
        "date": datetime.utcnow().isoformat(),
        "demo_cost": demo_cost
    }
    file_name = f"cost-report-{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(report)
    )

    # 2. Publish metric to CloudWatch
    cloudwatch.put_metric_data(
        Namespace='Demo/CostCalculator',
        MetricData=[
            {
                'MetricName': 'DemoCost',
                'Value': demo_cost,
                'Unit': 'None'
            },
        ]
    )

    # 3. Send SNS alert if cost > 0.8
    if demo_cost > 0.8:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Demo Cost Alert",
            Message=f"Demo cost reached {demo_cost} USD"
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Cost simulation completed!')
    }

