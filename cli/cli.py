import click as click
from lol.database.database import Database
from lol.datatypes.array import Array
from lol.prompt import Prompt
from clint.textui import colored as Color
import os as os
import json as JsonConverter

# the env identifier
identifier = "LOLDATABASES"



def remove_spaces(data):
    return_array = []
    for index, el in enumerate(data):
        if el is not " ":
            return_array.append(el)
    return return_array

class ArgumentParser():
    def __init__(self, command, param):
        # the functions that need to be executed
        self.command = command

        # the function paramete
        self.parameter = param

        # conditions
        self.databases = self.__get_all_databases(os.getcwd())
        self.current_databases = Array(Database)
        self.activated_databases = Array(Database)

        self.__execute_commands()

        print(self.databases)

    # get all databases in the current library
    def __get_all_databases(self, directory):
        # all files that end with a .lol extension
        LOL_FILES = []

        # loop through all files and check
        # for files that has a extension
        # (.lol)
        for index, folder_name in enumerate(os.listdir(directory)):
            # if the the file is actualy a file or a folder
            is_file = os.path.isfile(os.path.join(directory, folder_name))
            if folder_name.endswith(".lol") and is_file:
                LOL_FILES.append(folder_name)

        return LOL_FILES

    # create a new database object
    def create(self, database_name):
        # prompt for the fields
        data = Prompt("Enter the fields separated by spaces").prompt()

        # remove all the duplicate fields
        fields = Array.create(remove_spaces(data.split(" "))).get()

        
        database = Database(database_name, fields)
        self.current_databases.add(database)


    # check and execute all the commands
    def __execute_commands(self):
        command = self.command
        if command == "create":
            self.create(self.parameter)
        
        

@click.command()
@click.argument('command', type=str)
@click.argument('parameter', type=str)
def main(command, parameter):
    argument_parser = ArgumentParser(command, parameter)

if __name__ == "__main__":
    main()
