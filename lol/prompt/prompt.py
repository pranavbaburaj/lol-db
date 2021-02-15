from clint.textui import colored as Color
import getpass as PasswordPrompt


# the main prompt
class Prompt():
    def __init__(self, prompt_query="Enter something", email=False, password=False, typeof=str):
        # the prompt message used to query
        self.prompt_message = prompt_query

        self.email = email
        self.password = password
        self.typeof = typeof

        self.prompt()

    # create the prompt message 
    def prompt(self):
        print(Color.cyan(f"{self.prompt_message} [?] "), end='')
        if self.password == True:
            user_input = PasswordPrompt.getpass(prompt="")
        else:
            user_input = self.typeof(input(""))

        return self.verify_answer(user_input)

    # verify the input by user
        
