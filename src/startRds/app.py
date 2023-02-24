import boto3
import os
TAG = os.environ.get('TAG')

rds = boto3.client('rds')

def lambda_handler(event, context):

    print("Check RDS's tags")

    instances = rds.describe_db_instances()

    startInstances = []
    for instance in instances["DBInstances"]:

        tags = rds.list_tags_for_resource(ResourceName=instance["DBInstanceArn"])

        for tag in tags["TagList"]:

            if tag['Key'] == 'AutoRun':

                if tag['Value'] == TAG and instance['DBInstanceStatus'] == 'stopped':
                    print(instance)
                    startInstances.append(instance["DBInstanceIdentifier"])
                    print("STARTING:", instance["DBInstanceIdentifier"])
                    rds.start_db_instance(
                        DBInstanceIdentifier=instance["DBInstanceIdentifier"])

                    pass

                pass

    if len(startInstances) > 0:
        print("Success started RDS instances")
    else:
        print("No rds instances to shutdown.")
