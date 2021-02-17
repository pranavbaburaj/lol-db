from lol.prompt import Prompt
from clint.textui import colored as Color
import os as os

# the project class
class Project:
    def __init__(self):
        self.prompt_message = self.create_prompts()

        print(self.prompt_message)

    # create all the required prompts
    def create_prompts(self):
        prompt_solutions = {}
        prompt_queries = [
            "Project Name", 
            "License",
        ]

        for index, el in enumerate(prompt_queries):
            prompt = Prompt(el, typeof=str)
            prompt_solutions[
                str(el).replace(" ", "-").lower()
            ] = prompt.prompt().replace(" ", "_")

        if prompt_solutions['project-name'] == ".":
            prompt_solutions['project-name'] = os.path.basename(
                os.getcwd()
            )
            prompt_solutions['location'] = os.getcwd()
        else:
            prompt_solutions['location'] = os.path.join(
                os.getcwd(), prompt_solutions[
                    'project-name'
                ]
            )

        return prompt_solutions


def main():
    project = Project()


if __name__ == "__main__":
    main()