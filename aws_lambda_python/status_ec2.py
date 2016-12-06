# -*- Coding: utf-8 -*-
from __future__ import print_function

import boto3

print('Loading function')


def lambda_handler(event, context):
    print("start!!")
    print(event)
    pathparam = event['params']['path']
    instance = pathparam['instanceId']
    print("make instance client")
    ec2Client = boto3.resource('ec2')
    instanceClient = ec2Client.Instance(instance)

    print("get instance status")
    state = instanceClient.state['Name']

    response = "{ """"%s"""" : """"%s"""" }" % (instance, state)

    return response
