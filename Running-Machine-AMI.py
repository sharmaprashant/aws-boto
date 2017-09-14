__author__ = "Prashant Sharma"
__email__ = "prashant.aws@gmail.com"

import boto3
import botocore
import sys
instance_id = sys.argv[1]
ec2ServerImage = boto3.client('ec2', 'ap-southeast-2')
response = ec2ServerImage.describe_instances(InstanceIds=[instance_id])


def Create_Image(ami_name):
    AMI_ID = ec2ServerImage.create_image(InstanceId=instance_id, Name=ami_name, Description='Created by Automated Boto Script', NoReboot=True, DryRun=False)
    print AMI_ID


try:
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            status = (instance["State"]["Name"])
            if status == 'running':
                print "Machine Is Running and Initating the AMI Now without reboot"
                Create_Image(*sys.argv[2:])
            else:
                print "no"
except botocore.exceptions.ClientError as e:
    print e
