import boto3
import os
TAG = os.environ.get('TAG')

rds = boto3.client('rds')

def lambda_handler(event, context):

    print("Check RDS's tags")

    instances = rds.describe_db_instances()

    stopInstances = []
    for instance in instances["DBInstances"]:

        tags = rds.list_tags_for_resource(ResourceName=instance["DBInstanceArn"])

        for tag in tags["TagList"]:

            if tag['Key'] == 'AutoOff':

                if tag['Value'] == TAG and instance['DBInstanceStatus'] == 'stopped':
                    print(instance)
                    stopInstances.append(instance["DBInstanceIdentifier"])
                    print("STOPPING:", instance["DBInstanceIdentifier"])
                    rds.stop_db_instance(
                        DBInstanceIdentifier=instance["DBInstanceIdentifier"])

                    pass

                pass

    if len(stopInstances) > 0:
        print("Success stopped RDS instances")
    else:
        print("No rds instances to shutdown.")
