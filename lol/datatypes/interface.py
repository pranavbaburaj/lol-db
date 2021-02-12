# the interface
# class, or the interface
# data type

# interface data types
# are inspired from
# the typescript language

# example
# f = Interface(types)
# f.create(data)


class InterfaceObject():
    def __init__(self, object_info):
        # the passed in values
        # to create a new object
        self.values = object_info

    # get the interface
    # property
    def get_item(self, property_):
        if property_ in self.values:
            return self.values[property_]
        else:
            raise KeyError(f"Cannot find {property_}")

    # set the interface
    # property

    # Note : cannot change types after assignment
    def set_item(self, property_, value):
        # check if property_ is in self.values
        # if yes, pass
        # else throw a KeyError
        if property_ in self.values:
            # check whether the current type
            # of the key and the new type is same
            # if yes , change the value
            # else , raise  a KeyError
            typeof = isinstance(value, type(self.values[property_]))

            if typeof:
                self.values[property_] = value
            else:
                raise TypeError("Cannot change types after assignment")
        else:
            raise KeyError(f"Cannot find {property_}")

    def __repr__(self):
        return ""


class Interface(object):
    def __init__(self, data_params):
        # the main
        # key names and the
        # type of the value

        self.params = self.__get_params(data_params)

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

    # create a new interface
    # object
    def create(self, *args):
        # self.match = self.__match_param_types(data)
        # print(args)
        if len(args) == len(self.params):
            match = self.__match_param_types(args)
            return InterfaceObject(match)
        else:
            raise Exception(
                f"Expected {len(self.params)} arguments but got {len(args)}")

    # check whether
    # the new create interface
    # parameter type match
    # with self.params
    def __match_param_types(self, data):
        # check if the passed in
        # parameter is a
        # tuple, else throw
        # a TYpeError
        if isinstance(data, tuple):
            # the new interface
            interface = {}
            # loop through each element
            # and index in the dictionary
            # (self.params)
            for index, key in enumerate(self.params):
                # the current character
                # of the argument
                current_character = data[index]

                # the number of types
                # matches(a list of
                # True and False(booleans))
                types_matches = []
                for allowed_type in self.params[key]:
                    # if the allowed types
                    # is (?) or 'any', append true
                    # as it resembles (any) type

                    # else, if the type of
                    # the param is in
                    # the list of types
                    # allowed
                    if allowed_type == "?" or allowed_type == "any":
                        types_matches.append(True)
                    else:
                        types_matches.append(allowed_type == type(data[index]))
                # if the list is full of False
                # or if no types match raise
                # a type error
                # else, add it to the
                # interface dict
                if True not in types_matches:
                    raise TypeError("Types don't match")
                else:
                    interface[key] = data[index]
            # return the interface dict
            return interface

        else:
            raise TypeError("Expected a dict")
