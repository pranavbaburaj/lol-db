import click as click
from lol.database.database import Database
from lol.datatypes.array import Array
from lol.prompt import Prompt
from clint.textui import colored as Color
import os as os

# the env identifier
identifier = "LOLDATABASES"


# remove spaces from
# an array an return an array
# without spaces
def remove_spaces(data):
    """
    Create a return array and enumerate
    through the array and append it to
    the return array if the element is
    not a space( )
    """
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

    # get all databases in the current library
    def __get_all_databases(self, directory):
        # all files that end with a .lol extension
        LOL_FILES = []

        # loop through all files and check
        # for files that has a extension
        # (.lol)
        if os.path.exists(directory) and os.path.isdir(directory):
            for index, folder_name in enumerate(os.listdir(directory)):
                # if the the file is actualy a file or a folder
                is_file = os.path.isfile(os.path.join(directory, folder_name))
                if folder_name.endswith(".lol") and is_file:
                    LOL_FILES.append(os.path.join(directory, folder_name))

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
        # make a duplicate of the self.command
        command = self.command
        if command == "create":
            """
            if command is craete,
            create the database
            """
            self.create(self.parameter)
        elif command == "list":
            """
            if the command is list and if
            the parameter is a . take the lolfiles
            in the current folder, else, 
            do the same with the given parameter
            """
            if self.parameter == ".":
                data = self.__get_all_databases(os.getcwd())
            else:
                data = self.__get_all_databases(self.parameter)

            for index, file in enumerate(data):
                string = f"[{index + 1}] {file} "
                if os.path.isfile(file):
                    print(Color.green(f"{string}(LOLFILE)"))
        elif command == "remove" or command == "delete":
            """
            Removing a file if it exists
            in the current directory, 
            else throw out an error
            """
            filename = f"{self.parameter}.lol"
            if filename in os.listdir(os.getcwd()):
                os.remove(os.path.join(os.getcwd(), filename))
            else:
                print(
                    Color.red(
                        f"Cannot find {os.path.join(os.getcwd(), filename)}"))


@click.command()
@click.argument('command', type=str)
@click.argument('parameter', type=str)
def main(command, parameter):
    argument_parser = ArgumentParser(command, parameter)


if __name__ == "__main__":
    main()
