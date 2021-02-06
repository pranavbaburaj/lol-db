
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

    # get the length of the map
    def length(self):
        return len(self.__dict)

    # delete the map item
    # based on the parameter
    # passed in
    def delete(self, delete_key):
        # check if the specified
        # key is present in the
        # map

        # if true delete it and return 
        # the map
        # else raise an Exception
        if delete_key in self.__dict:
            del self.__dict[delete_key]
            return self.get()
        else:
            raise Exception(f"Cannot find key {delete_key}")

    # filter the map
    # for a specific
    # value
    def filter(self, filter_value):
        # loop through each dict
        # keys and if the value 
        # match append it to the array
        # and return it
        find_arr = []

        for dict_key in self.__dict:
            if self.__dict[dict_key] == filter_value:
                find_arr.append(dict_key)
        return find_arr

    def clear(self):
        self.__dict = {}
        return self.get()

    # change a specific value
    def change(self, k, i):
        if k in self.__dict:
            if isinstance(i, self.types[1]):
                self.__dict[k] = i
        
        