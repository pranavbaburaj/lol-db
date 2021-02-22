import sys

def remove_spaces(remove_space_array):
    element_array = []
    for element in remove_space_array:
        if element is not " ":
            element_array.append(element)

    return element_array

class Parser:
    def __init__(self, commands):
        self.parse_items = sys.argv[1:]
        self.commands = self.__is_valid_commands(commands)

    def __is_valid_commands(self, commands):
        assert isinstance(commands, list), "Expected type list"

        for element_index, element in enumerate(commands):
            if isinstance(element, dict):
                dict_element_keys = [key for key in element]
                element["value"] = remove_spaces(
                    element["value"].split(" ")
                )
                print(element)
            else:
                raise TypeError("Expected a dict")