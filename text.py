import boto3
import random
import os

region = os.environ['PHONE_REGION']
phone = os.environ['PHONE']
sns = boto3.client('sns', region_name=region)


def text(message):
    sns.publish(PhoneNumber=phone, Message=message)
