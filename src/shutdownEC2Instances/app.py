import boto3
import logging
import os
TAG = os.environ.get('TAG')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    print('TAG:', {TAG})

    filters = [{
            'Name': 'tag:AutoOff',
            'Values': [TAG] #20:00
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)

    RunningInstances = [instance.id for instance in instances]

    print(RunningInstances)

    if len(RunningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print (shuttingDown)
    else:
        print ("Nothing to see here")