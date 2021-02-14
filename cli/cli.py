import click

@click.command()
@click.argument('command', type=str)
@click.argument('name', type=str)
def main(command, name):
    print(f"{command} {name}")