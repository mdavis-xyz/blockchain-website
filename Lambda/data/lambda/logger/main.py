import logging
import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
import decimal
import datetime as dt
import pprint as pp
import json

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("----")
    logger.info("servejson Event:" + str(event).replace('\n',' '))
    logger.info("servejson Content:" + str(context).replace('\n',' '))

    response = {
      'statusCode': 200  ,
      'headers' : {"Access-Control-Allow-Origin": "*"}
    }

    return(response)
