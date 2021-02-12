# switch cases are a type of
# conditional statements


class SwitchCases():
    def __init__(self, data, switch_case_dict):
        # all the conditions
        # and functions for the
        # conditions
        self.__cases = self.__get_cases(switch_case_dict)

        # the variable value that we
        # have to compare
        self.data = data

    # compare the cases and return a
    # specific function
    def compare(self):
        self.__cases = self.remove_duplicate_cases(self.__cases)
        if self.data in self.__cases:
            return self.__cases[self.data]
        else:
            if None not in self.__cases:
                self.__cases[None] = self.default_case

            return self.__cases[None]

    # cannot find function
    def default_case(self):
        print("Cannot find mathing keys")

    # validate the switch cases
    def __get_cases(self, cases):
        # check if the type f cases
        # == dict, if yes, loop through
        # each list item and check whether
        # they are functions, else throw an Error
        if isinstance(cases, dict):
            for element in cases:
                if not callable(cases[element]):
                    raise TypeError(f"{element} is not a function")
            return cases
        else:
            # throw an error
            raise TypeError("Expected a dict")

    # remove duplicate cases from
    # the dict
    def remove_duplicate_cases(self, cases):
        small_dict = {}
        for key in cases:
            # loop through each key and
            # add it to the small_dict
            # if not present in it
            if key not in small_dict:
                small_dict[key] = cases[key]

        # return the small_dict
        return small_dict


# call the switch evaluator
def switch(switch_variable, conditions):
    switch_case = SwitchCases(switch_variable, conditions)

    return switch_case.compare()
