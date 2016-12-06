# -*- Coding: utf-8 -*-
from __future__ import print_function

import json
import urlparse
import boto3

print('Loading function')


def lambda_handler(event, context):
    print("start!!")
    print(event)
    pathparam = event['params']['path']
    instance = pathparam['instanceId']
    print(instance)
    print("make instance client")
    ec2Client = boto3.resource('ec2')
    instanceClient = ec2Client.Instance(instance)

    print("get instance status")
    state = instanceClient.state['Name']
    print(state)

    idList = []
    if state == "running":
        idList.append(instance)
        res = ec2Client.instances.filter(InstanceIds=idList).stop()
        return {"result": "success to stop instance"}
    else:
        return {"result": "target instance is already stopped or stopping"}