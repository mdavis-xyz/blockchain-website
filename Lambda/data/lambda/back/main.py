import logging
import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
import decimal
import datetime as dt
import pprint as pp
import json
import time
import os
from random import randint
import traceback as tb

# dynamodb requires a hash key
# not just sort key
# just use hash as 0 for all records
hash_const = 0

def unit_tests():
    print('No unit tests to run')

def lambda_handler(event,context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if ('unitTest' in event) and event['unitTest']:
        logger.info('Running unit tests')
        unit_tests()
        return()
    else:
        logger.info('Running main (non-test) handler')
        return(main(logger,event))


def main(logger,event):
    logger.setLevel(logging.INFO)
    #logger.info("----")
    logger.info("logger view count Event:" + str(event).replace('\n',' '))
    #logger.info("servejson Content:" + str(context).replace('\n',' '))
    #uid = event['requestId']

    try:
        timestamp = int(event['requestTimeEpoch'])
    except KeyError as e:
        logger.warn("could't find requestTimeEpoch")
        timestamp = int(time.time())

    try:
        increment(logger,timestamp) 
    except Exception as e:
        logger.warn("failed to increment database, sleeping then retrying")
        tb.print_tb(e.__traceback__)
        time.sleep(5+randint(0,20)) # add randomness so if it's concurrancy that's the issue, we avoid it the 2nd time 
        increment(logger,timestamp)       

    response = {
      'statusCode': 200  ,
      'headers' : {"Access-Control-Allow-Origin": "*"},
      'body': json.dumps({"foo":"bar"})
    }

    return(response)

def increment(logger,timestamp):
    try:
        table_name = os.environ['viewHistoryTable'] 
    except KeyError as e:
        print('environment vars:')
        print(sorted([x for x in os.environ.keys()]))
        raise(e)

    client = boto3.client('dynamodb')

    logger.info('saving view log to dynamo for time %s' % str(timestamp))

    response = client.update_item(
        TableName=table_name,
        Key={
            'hash': {
                'N': str(hash_const)
            },
            'time': {
                'N': str(int(timestamp)) # boto requires str for ints
            }
        },
        UpdateExpression='ADD viewcount :q',
        #ExpressionAttributeNames={
        #    'N': 'count'
        #},
        ExpressionAttributeValues={
            ':q': {
                'N': '1'
            }
        }
    )
    logger.info('database incremented')

if __name__ == '__main__':
    now = int(time.time())
    #now = 1234
    logger = logging.getLogger()
    increment(logger,now)
