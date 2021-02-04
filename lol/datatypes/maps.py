
class Maps:
    def __init__(self, map_types):
        self.types = self.get_map_data_type(map_types)

        # the dictionary
        self.__dict = {}

    # get the data types of the map
    def get_map_data_type(self, types):
        # check the type of the
        # types parameter and
        # return the tuple
        # as a sliced list
        if isinstance(types, tuple):
            return list(types[0:2])
        else:
            raise TypeError("Invalid type")
    
    # add an item to the 
    # map
    def add(self, add_item_key, add_item_value):
        # check whether the types
        # match to the specified
        # types and add it to
        # the dict
        if isinstance(add_item_key, self.types[0]) and isinstance(add_item_value, self.types[1]):
            if add_item_key not in self.__dict:
                self.__dict[add_item_key] = add_item_value
        else:
            raise TypeError("Types don't match")

    def get(self):
        return self.__dict

    def has(self, key_item):
        # check whether a specified
        # key is present in the dictionary
        # and return a boolean value
        return key_item in self.__dict