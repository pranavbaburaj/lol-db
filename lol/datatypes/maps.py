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
        if isinstance(add_item_key, self.types[0]) and isinstance(
                add_item_value, self.types[1]):
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

    # convert a list to array
    @staticmethod
    def create(convert):
        # if the object is a list
        # create a map object and for
        # each element in the list
        # map[index] = elemetn
        if isinstance(convert, list):
            small_dict = {}
            for index, element in enumerate(convert):
                small_dict[index] = str(element)
            return Maps.get_map_object(int, str, small_dict)
        elif isinstance(convert, dict):
            # if the length of the convert
            # dict is 0 return the map
            # object of type string
            if len(convert) == 0:
                return Maps.get_map_object(str, str, convert)
            else:
                # get all the keys in the dict
                all_keys = [key for key in convert]

                # the type of the key
                key = type(all_keys[0])

                # the type of the value
                value = type(convert[all_keys[0]])

                all_values = [convert[k] for k in convert]

                # for all element in keys
                # if the type of keys is not
                # equal convert all keys to strings
                for element in all_keys:
                    if not isinstance(element, key):
                        for i in range(len(all_keys)):
                            all_keys[i] = str(all_keys[i])

                # for all element in values
                # if the type of value is not
                # equal convert all values to strings
                for idx, el in enumerate(all_values):
                    if not isinstance(el, value):
                        for el_object in range(len(all_values)):
                            all_values[el_object] = str(all_values[el_object])

                small_dict = {}
                # create a dict and for each index in
                # all_keys and all_values
                # all_keys[idx] = all_values[idx]
                for index, el in enumerate(all_keys):
                    small_dict[el] = all_values[index]

                # return a new map object
                return Maps.get_map_object(type(all_keys[0]),
                                           type(all_values[0]), small_dict)
        else:
            # if the type is not a list or a
            # dict throw an error
            raise TypeError("Create method expected a list or a dict")

    # get a new map object
    def get_map_object(key, value, value_dict):
        map_object = Maps((key, value))

        # add all dict items to the
        # map objecta nd return it
        for key_value in value_dict:
            map_object.add(key_value, value_dict[key_value])

        return map_object
