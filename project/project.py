from lol.prompt import Prompt
from clint.textui import colored as Color
import os as os

# get the mit license


def mit_license():
    return """
    MIT License

    Copyright (c) 2021 Pranav Baburaj

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """


# the project class
class Project:
    def __init__(self):
        # create all the prompt message
        self.prompt_message = self.create_prompts()

        # create all the required directories

        self.create_directories(self.prompt_message)

    # create all the directories
    def create_directories(self, data):
        # check if the filename already exists
        dir_exists = os.path.exists(data['location'])

        # if the directory exists throw out an
        # error
        if dir_exists:
            # but if the location is the current
            # directory it is always created
            # so we check if it is empty
            # if not throw out an error
            if data['location'] is not os.getcwd():
                if len(os.listdir(data['location'])) > 0:
                    print(Color.red("[ERROR] : Folder is not empty"))
            else:
                print(Color.red("[ERROR] : File or folder already exists"))
        else:
            # create the location directory
            os.mkdir(data['location'])

            # create the license file
            self.create_license_file(data['location'], data['license'])

    # create the license file
    def create_license_file(self, location, license_file):
        # check if the license is mit
        # if yes, write the mit license to the file
        # else create an empty file
        if license_file == "mit":
            license_data = mit_license()
        else:
            license_data = "LICENSE"
        filename = os.path.join(location, "LICENSE")
        with open(filename, "w") as license_writer:
            license_writer.write(license_data)

    # create all the required prompts
    def create_prompts(self):
        # the answers given by the user
        prompt_solutions = {}

        # all the questions to ask to
        # the user
        prompt_queries = [
            "Project Name",
            "License",
        ]

        # for each query in prompt_queries
        # prompt the query and add it to the
        # prompt_solution
        # prompt_solution[query] = retort
        for index, el in enumerate(prompt_queries):
            prompt = Prompt(el, typeof=str)
            prompt_solutions[str(el).replace(
                " ", "-").lower()] = prompt.prompt().replace(" ", "_")

        # check if the project name is a dot(.)
        # if yes, change it the directory basename
        # and add a new key called location(os.getcwd()) to
        # the prompt_solutions
        # else, create a new key called location
        if prompt_solutions['project-name'] == ".":
            prompt_solutions['project-name'] = os.path.basename(os.getcwd())
            prompt_solutions['location'] = os.getcwd()
        else:
            prompt_solutions['location'] = os.path.join(
                os.getcwd(), prompt_solutions['project-name'])

        # convert the variable into
        # lowercase text
        prompt_solutions['license'] = prompt_solutions['license'].lower()

        return prompt_solutions


def main():
    # create a new project
    project = Project()


if __name__ == "__main__":
    main()