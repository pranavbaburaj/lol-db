import click as click
from lol.database.database import Database
from lol.datatypes.array import Array
from clint.textui import colored as Color
import os as os

class ArgumentParser():
    def __init__(self, command, param):
        # the functions that need to be executed
        self.command = command

        # the function paramete
        self.parameter = param

        # conditions
        self.databases = self.__get_all_databases(os.getcwd())
        self.activated_databases = Array(Database)

        print(self.activated_databases)

    # get all databases in the current library
    def __get_all_databases(self, directory):
        return []
        


@click.command()
@click.argument('command', type=str)
@click.argument('parameter', type=str)
def main(command, parameter):
    argument_parser = ArgumentParser(command, parameter)

if __name__ == "__main__":
    main()
