import sys

def remove_spaces(remove_space_array):
    element_array = []
    for element in remove_space_array:
        if element is not "":
            element_array.append(element)

    return element_array

def has_duplicate_variables(variables):
    for element in variables:
        if variables.count(element) > 1:
            return True
    return False

class Parser:
    def __init__(self, commands):
        self.arguments = sys.argv[1:]
        self.commands = self.__is_valid_commands(commands)


    def __is_valid_commands(self, commands):
        assert isinstance(commands, list), "Expected type list"

        for element_index, element in enumerate(commands):
            if isinstance(element, dict):
                dict_element_keys = [key for key in element]
                element["value"] = remove_spaces(
                    element["value"].split(" ")
                )

                variables = list(filter(
                    lambda val : val.startswith("$"),
                    element["value"]
                ))

                assert not has_duplicate_variables(
                    variables
                ), "The Parameter contains duplicate variables"

                if not "types" in element:
                    element["types"] = {}
                else:
                    assert isinstance(element["types"], dict), "Expected the types to be a dict"
                
                for index, item in enumerate(element["value"]):
                    if item in variables:
                        if item[1:] in element["types"]:
                            element["value"][index] = {
                                "value" : item[1:],
                                "type" : element["types"][item[1:]]
                            }
                        else:
                            element["value"][index] = {
                                "value" : item[1:],
                                "type" : str
                            }
                assert "func" in element, "Cannot find key func"
                assert callable(element["func"]), "func not a function"

            else:
                raise TypeError("Expected a dict")
        return commands

    def parse(self):
        for each_command in self.commands:
            command_value = each_command["value"]
            if len(self.arguments) == len(command_value):
                all_cases_match = False
                for index in range(len(self.arguments)):
                    if isinstance(command_value[index], str):
                        if command_value[index] == self.arguments[index]:
                            all_cases_match = True
                        else:
                            all_cases_match = False
                    else:
                        pass
                if all_cases_match:
                    return each_command["func"](
                        self.__get_variable_values(
                            each_command,
                            self.arguments
                        )
                    )
                    
            else:
                pass

    def __get_variable_values(self, command, arguments):
        data = command["value"]
        variables = {}
        for index in range(len(data)):
            element = data[index]
            if isinstance(element, dict):
                variables[element["value"]] = arguments[index]
                
        return dict(variables)

        
