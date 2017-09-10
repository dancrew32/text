import boto3
import log
import random
import os

region = os.environ['PHONE_REGION']
my_phone = os.environ['PHONE']
bub_phone = os.environ['PHONE_BUB']
sns = boto3.client('sns', region_name=region)


def me(message):
    sns.publish(PhoneNumber=my_phone, Message=message)
    log.log(message)


def bub(message):
    sns.publish(PhoneNumber=bub_phone, Message=message)
    log.log(message)

