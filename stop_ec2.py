# -*- Coding: utf-8 -*-
from __future__ import print_function

import json
import urlparse
import boto3


def start_instance(client, instanceId):
    idList = []
    idList.append(instanceId)
    return client.instances.filter(InstanceIds=idList).stop()

def get_stopping_instances(client):
    targetList = []
    instances = client.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        targetList.append(instance.id)
    return targetList

print('Loading function')
def lambda_handler(event, context):
    print("start!!")
    toStartList = []
    instances = event['instanceIds']

    print("make instance")
    ec2Client = boto3.resource('ec2')

    print("get stopping instances")
    stopping_instances = get_stopping_instances(ec2Client)
    print(stopping_instances)
    for stopping_instance in stopping_instances:
        if stopping_instance in instances:
            toStartList.append(stopping_instance)
            print("instance %s need to start" % stopping_instance)

    for toStart in toStartList:
        response = start_instance(ec2Client, toStart)
        print("start instance:%s " % toStart)
        print("response:%s " % response)

    print("end")
    return toStartList
