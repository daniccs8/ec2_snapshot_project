import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')


@click.group('volumes')
def cli():
    """script for manages snapshots"""

########################################### Group volumes

@cli.group('volumes')
def volumes():
    """commands for volumes"""

@volumes.command('list')
@click.option('--state', default="running", help='List all EC2 in running state for volumes')
def list_volumes(state):
    """commands for list instances state"""
    instance_s = []
    "list all EC2 runnning"
    if state:
        filter1 = [{'Name': 'instance-state-name', 'Values':[state]}]
        instance_s = ec2.instances.filter(Filters=filter1)

    else:
        instance_s = ec2.instances.all()

    for i in instance_s:
        for v in i.volumes.all():
            print(', '.join((
                v.id,
                i.id,
                str(v.size) + "GiB",
                v.state
            )))
    return

########################################### Group snapshots

@cli.group('snapshots')
def snapshots():
    """commands for snapshots"""

@snapshots.command('list')
@click.option('--state', default="running", help='List snapshot of ec2 volumes running')
def create_snapshot(state):
    """List snapshot of ec2 volumes running"""
    volume_s = []
    "list all EC2 runnning"
    if state:
        filter1 = [{'Name': 'instance-state-name', 'Values':[state]}]
        volume_s = ec2.instances.filter(Filters=filter1)

    else:
        volume_s = ec2.instances.all()

    for i in volume_s:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(', '.join((
                    i.id,
                    v.id,
                    v.state,
                    s.id,
                    s.state,
                    s.progress,
                    s.start_time.strftime('%c'),
                 )))

    return

########################################### Group instances

@cli.group('instance')
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
        cli()
