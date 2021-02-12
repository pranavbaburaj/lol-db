
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

        print(self.__cases)

    # compare the cases and return a
    # specific function 
    def compare(self):
        pass

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

# call the switch evaluator
def switch(switch_variable, conditions):
    switch_case = SwitchCases(
        switch_variable,
        conditions
    )
