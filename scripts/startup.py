import datetime
import time
import boto3


class ContainerBootTimer:
    def __init__(self, client):
        self.client = client

    def start(self):
        self.taskResp = self.client.run_task(
            taskDefinition='gbmperf-task:12',
            count=1,
            launchType='FARGATE',
            platformVersion='1.4.0',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0b937c7fd7b184cdb'],
                    'securityGroups': ['sg-00e191eb5d200f0e6'],
                    'assignPublicIp': 'ENABLED'
                }
            }
        )['tasks'][0]

        self.start = datetime.datetime.now()
        print(self.taskResp['taskArn'], self.start)

    def wait(self):
        while True:
            task = self.client.describe_tasks(
                cluster=self.taskResp['clusterArn'],
                tasks=[self.taskResp['taskArn']]
            )['tasks'][0]
            if task['lastStatus'] == 'RUNNING':
                self.end = task['startedAt'].replace(tzinfo=None)
                break
            time.sleep(2)

        self.client.stop_task(task=self.taskResp['taskArn'])

        self.time = self.end - self.start


class VMBootTimer:
    def __init__(self, client):
        self.client = client

    def start(self):
        
        self.runResp = self.client.run_instances(
            MaxCount=1,
            MinCount=1,
            ImageId='ami-08679cab36008bdff',
            InstanceType='m5.xlarge',
            SecurityGroupIds=[
                'sg-0dfe71d4d563d518a',
            ],
            KeyName='mludwig'
        )['Instances'][0]
        self.start = datetime.datetime.now()
        print(self.runResp['InstanceId'], self.start)

    def wait(self):
        while True:
            task = self.client.describe_tasks(
                cluster=self.taskResp['clusterArn'],
                tasks=[self.taskResp['taskArn']]
            )['tasks'][0]
            if task['lastStatus'] == 'RUNNING':
                self.end = task['startedAt'].replace(tzinfo=None)
                break
            time.sleep(2)

        self.client.stop_task(task=self.taskResp['taskArn'])

        self.time = self.end - self.start


def ecs_test():
    client = boto3.client('ecs')
    timers = []

    for _ in range(5):
        timer = ContainerBootTimer(client)
        timer.start()
        timers.append(timer)

    # for timer in timers:
    #     timer.wait()
    
    return timers


def ec2_test():
    client = boto3.client('ec2')
    timers = []

    for _ in range(1):
        timer = VMBootTimer(client)
        timer.start()
        timers.append(timer)

    # for timer in timers:
    #     timer.wait()
    
    return timers


test = 'ec2'
if test == 'ecs':
    timers = ecs_test()
elif test == 'ec2':
    timers = ec2_test()

# avg = sum((t.time for t in timers), datetime.timedelta()) / len(timers)
# print(avg)