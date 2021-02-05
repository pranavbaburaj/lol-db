# the interface
# class, or the interface
# data type

# interface data types
# are inspired from
# the typescript language

# example
# f = Interface(types)
# f.create(data)

class Interface(object):
    def __init__(self, data_params):
        # the main
        # key names and the
        # type of the value

        self.params = self.__get_params(data_params)

        print(self.params)

    # verifying the entered 
    # parameters and return
    # them
    def __get_params(self, data):
        # check whether the data
        # passed in is a dict
        # else throw an Error
        data_is_dict = isinstance(data, dict)

        # loop through each dict
        # value and check whether
        # each value is
        # a list
        # the list of types it can be
        # return the passed-in parameter
        if data_is_dict:
            for data_key in data:
                if not isinstance(data[data_key], list):
                    raise TypeError("Expected to be a list")
            return data
        else:
            raise TypeError("Expected a dict")
