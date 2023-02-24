import boto3
import logging
import os
TAG = os.environ.get('TAG')

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    print('TAG:', {TAG})
    filters = [{
            'Name': 'tag:AutoRun',
            'Values': [TAG]
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    StoppedInstances = [instance.id for instance in instances]
    print(StoppedInstances)
    #print the instances for logging purposes
    #print RunningInstances 
    
    #make sure there are actually instances to shut down. 
    if len(StoppedInstances) > 0:
        #perform the shutdown
        start = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print (start)
    else:
        print ("Nothing to see here")