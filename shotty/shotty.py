import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
@click.option('--listec2', default=None, help='List all EC2 in project: <thebestone>')
def list_instances(listec2):
        "list EC2 instances"
        instance_s = []
        if listec2:
            filters_ = [{'Name': 'tag:Project', 'Values':[listec2]}]
            instance_s = ec2.instances.filter(Filters=filters_)

        else:
            instance_s = ec2.instances.all()

        for i in instance_s:
          print (', '.join((
                 i.id,
                 i.instance_type,
                 i.placement['AvailabilityZone'],
                 i.state['Name'],
                 i.public_dns_name)))
        return

if __name__ == '__main__':
        list_instances()
