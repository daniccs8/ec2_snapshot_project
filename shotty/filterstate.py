import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.group()
def istate():
        """commands for list instances state"""

@istate.command("stopped")
@click.option('--state', default="stopped", help='List all EC2 in stopped state')
def ec2state_stopped(state):
    instance_s = []
    "list all EC2 stopped"
    if state:
        filter1 = [{'Name': 'instance-state-name', 'Values':[state]}]
        instance_s = ec2.instances.filter(Filters=filter1)

    else:
        instance_s = ec2.instances.all()

    for i in instance_s:
        print(', '.join((
            i.id,
            i.placement['AvailabilityZone'],
            i.state['Name']
        )))

    return

@istate.command("running")
@click.option('--state', default="running", help='List all EC2 in stopped state')
def ec2state_running(state):
    instance_s = []
    "list all EC2 running"
    if state:
        filter1 = [{'Name': 'instance-state-name', 'Values':[state]}]
        instance_s = ec2.instances.filter(Filters=filter1)

    else:
        instance_s = ec2.instances.all()

    for i in instance_s:
        print(', '.join((
            i.id,
            i.placement['AvailabilityZone'],
            i.public_ip_address,
            i.state['Name']
        )))

    return

if __name__ == '__main__':
        istate()
