#!/bin/bash

YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# VARIABLES STANDAR
ENV=develop #THIS WORK FINE IF WE USE SAM IN LOCAL. IN PIPELINE IS NOT NEED

PROJECT=instance-scheduler #PROJECT NAME FOR THE TAGS
STACK=$PROJECT-$ENV #NAME OF STACK, IS IMPORTANT FOR THE NAME OF ALL OBJECTS IN TEMPLATE
AWS_PROFILE=winclap
BUCKET=$STACK-$AWS_PROFILE #BUCKET IS REQUIRED FOR SAM PACKAGE

REGION_1=us-east-1

echo "================== Create Bucket =================="
aws s3api create-bucket --bucket $BUCKET --profile $AWS_PROFILE

echo "${YELLOW} Validating local SAM Template..."
echo " ================================${NC}"
sam validate --profile $AWS_PROFILE --region $REGION_1 --template "template.yaml"

echo "${YELLOW} Building local SAM App..."
echo " =========================${NC}"
sam build --cached

echo "${YELLOW} Deploy"
echo " ================================================= ${NC}"
sam deploy --no-confirm-changeset --profile $AWS_PROFILE --s3-bucket $BUCKET --region $REGION_1 --capabilities CAPABILITY_NAMED_IAM --stack-name $STACK --tags Project=$PROJECT Environment=$Environment --parameter-overrides Project=$PROJECT Environment=$ENV

echo "${YELLOW} Empty temporaly bucket for SAM..."
echo " ================================================= ${NC}"
aws s3 --profile $AWS_PROFILE --region $REGION_1 rm s3://$BUCKET --recursive

echo "${YELLOW} Deleting temporaly bucket for SAM..."
echo " ================================================= ${NC}"
aws s3 --profile $AWS_PROFILE --region $REGION_1 rb s3://$BUCKET --force