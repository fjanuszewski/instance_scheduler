# Instance Scheduler SAM Template

This is a Serverless Application Model (SAM) template for an instance scheduler that shuts down and starts up Amazon EC2 instances and RDS databases based on a specified time schedule.

## AWS Resources

This template includes the following AWS resources:

- `ShutdownEC2Instance` - A Lambda function that shuts down EC2 instances based on a specified time schedule.
- `ShutdownRDS` - A Lambda function that shuts down RDS databases based on a specified time schedule.
- `StartEC2Instance` - A Lambda function that starts up EC2 instances based on a specified time schedule.
- `StartRDS` - A Lambda function that starts up RDS databases based on a specified time schedule.

## Global Configuration

The template includes global configuration settings for all Lambda functions, including:

- Timeout: 30 seconds
- MemorySize: 128 MB
- Tracing: Active
- Runtime: Python 3.9

## Resources Configuration

Each AWS resource in the template is configured with the following settings:

- `CodeUri`: the directory path for the function's code.
- `Handler`: the name of the Python function that handles the Lambda event.
- `Environment`: environment variables used in the function.
- `Policies`: the permissions required for the function to execute.
- `Events`: the event trigger for the function.

The `ShutdownEC2Instance` and `ShutdownRDS` functions are triggered by a cron event to shut down instances/databases at a specified time. The `StartEC2Instance` and `StartRDS` functions are triggered by a cron event to start up instances/databases at a specified time.

**Note**: The time schedules specified in the `TAG` variables are in UTC time, which is 3 hours ahead of Argentina time.
