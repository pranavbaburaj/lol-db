import click
from argument import ArgumentParser


@click.command()
@click.argument('command', type=str)
@click.argument('parameter', type=str)
def main(command, parameter):
    argument_parser = ArgumentParser(command, parameter)

