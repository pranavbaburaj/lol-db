import click

# all databases created
DATABASES = []

# database is activated or not
ACTIVATED_DATABASE = True

@click.command()
@click.argument('command', type=str)
@click.argument('name', type=str)
def main(command, name):
    if command == "create":
        pass