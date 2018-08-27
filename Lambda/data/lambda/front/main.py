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

# do this outside a function, so it caches it
html_fname = 'response.html'
with open(html_fname,'r') as f:
    html = f.read()
    assert(type(html) == type(''))

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
        timestamp = int(time.time())
        logger.warn("could't find requestTimeEpoch. Using %d instead" % timestamp)

    logger.info("Keys to event: %s" % str([x for x in event]))
    for x in ['pathParameters','queryStringParameters']:
        try:
           logger.info("Keys to event['%s']: %s" % (x,str([x for x in event[x]])))
        except:
           logger.info("Can't find " + x)
    try:
        websiteName =  event['queryStringParameters']['websiteName']
    except (KeyError,TypeError):    
        logger.error("Can't find websiteName")
        response = {
          'statusCode': 400  ,
          'headers' : {
             "Access-Control-Allow-Origin": "*",
             "Content-Type": "text/html"
          },
          'body': "Error, websiteName parameter missing"
        }
        return(response)

    sendMessage(logger,websiteName)

    response = {
      'statusCode': 200,
      'headers' : {
         "Access-Control-Allow-Origin": "*",
         "Content-Type": "text/html"
      },
      'body': html
    }

    return(response)

def sendMessage(logger,websiteName):
    logger.warn("Not actually sending message. TODO")
