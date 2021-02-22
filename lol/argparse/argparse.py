import sys

def remove_spaces(remove_space_array):
    element_array = []
    for element in remove_space_array:
        if element is not "":
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
                variables = list(filter(
                    lambda val : val.startswith("$"),
                    element["value"]
                ))

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
            else:
                raise TypeError("Expected a dict")
