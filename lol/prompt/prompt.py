from clint.textui import colored as Color
import getpass as PasswordPrompt
import re as EmailValidator


# the main prompt
class Prompt():
    def __init__(self,
                 prompt_query="Enter something",
                 verify=None,
                 typeof=str):
        # the prompt message used to query
        self.prompt_message = prompt_query

        self.verify = verify
        self.typeof = typeof

        # self.data = self.prompt()

    # create the prompt message
    def prompt(self):
        print(Color.cyan(f"{self.prompt_message} [?] "), end='')
        if self.verify == "password":
            user_input = PasswordPrompt.getpass(prompt="")
        else:
            user_input = self.typeof(input(""))

        return self.verify_answer(user_input)

    # verify the input by user
    def verify_answer(self, input_data):
        # verifying the user_input
        if isinstance(input_data, str):
            if self.verify == "password":
                if len(input_data) < 8:
                    print(Color.red("Passwords must be atleast 8 characters"))
                return input_data
            elif self.verify == "email":
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if not EmailValidator.search(regex, input_data):
                    print(Color.red("Invalid email"))

                return input_data
        else:
            return input_data
        return input_data

    # def get(self):
    #     return self.data
