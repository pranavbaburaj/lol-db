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

    def __print_message(self):
        print(Color.cyan(f"{self.prompt_message} [?] "), end='')

    # create the prompt message
    def prompt(self):
        self.__print_message()
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

    # create an option
    def option(self, options, repeat=True):
        if isinstance(options, list):
            self.__print_message()
            print("\n")
            for element_index in range(len(options)):
                current_element = options[element_index]
                if not isinstance(options[element_index], dict):
                    raise TypeError("Element expected to be a dict")
                else:
                    start_at_text = "[~]"
                    if "selector" in current_element:
                        start_at_text = f"[{current_element['selector']}]"
                    
                    print(Color.cyan(
                        f"{start_at_text} {current_element['prompt']}"
                    ))
                    
            print(Color.cyan("\n -> "), end='')
            user_input = input()

            for dict_element in options:
                match = str(user_input).lower() == str(dict_element['prompt'].lower()) 
                if match:
                    if "return" in dict_element:
                        return dict_element["return"]
                    else:
                        return dict_element["selector"]
            
            if repeat:
                return self.option(
                    options
                )
            else:
                return None
        else:
            raise TypeError("Options should be lists")

    # throw an error message
    @staticmethod
    def error(error_message):
        print(Color.red(f"[ERROR] {error_message}"))

    # def get(self):
    #     return self.data
