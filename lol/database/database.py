import os
import json
# the main database

# uuid is used
# to create unique
# user id(s)
import uuid

# logging module
# is used log
# errors and warnings
import logging as logger

# the table class
# used to create
# many tables in the database
# each table is represented
# by  a json file
# in the name of the table


class Database():
    def __init__(self, table_name, fields):
        self.table = self.__get_table_name(table_name)
        self.fields = self.__get_field_name(fields)

        # create the database
        self.filename = self.__create_new_database_file(self.table)

        # index of the data
        # or id of each data fields
        self.idx = 0

        # the main dictionary in which the data
        # is going to be stored
        self.__data_dict = self.__get_file_dict()

        # print(self.__data_dict)

        self.__commit_additions()

        self.modifications = True

        # print(self.filename)

    # get the table name
    def __get_table_name(self, table_name):
        """
        if the table_name is a string
        return the string(with all spaces replaced by underscores)

        else raise a TypeError
        """
        if isinstance(table_name, str):
            return table_name.replace(" ", "_")
        else:
            raise TypeError("Table name expected to be a string")

    # get all valid fields
    def __get_field_name(self, fields):
        final_fields = []
        if isinstance(fields, list):
            # for dict_key in fields:
            #     final_fields.append(
            #         {
            #             "name" : dict_key,
            #             "typeof" : fields[dict_key]
            #         }
            #     )
            for index, el in enumerate(fields):
                if isinstance(el, str):
                    if el not in final_fields:
                        final_fields.append(el)
                else:
                    raise TypeError("Each field must be a string")
            return final_fields
        else:
            raise TypeError("Fields are expected to be dicts")

    def __create_new_database_file(self, database):
        # create the database
        # file for storing the information
        filename = os.path.join(os.getcwd(), f"{database}.lol")
        if not os.path.exists(filename):
            with open(filename, "w") as create_file_object:
                json.dump({}, create_file_object)

        return filename

    # commit the changes to the
    # file
    # write the updated dictionary
    # to the file
    def __commit_additions(self):
        with open(self.filename, "w") as json_data_writer:
            json.dump(self.__data_dict, json_data_writer, indent=6)

    # add a new data to the
    # the self.dictionary and
    # commit the changes
    # (write it to the file)
    def add(self, data_to_save):
        # check if the parameter
        # is a list object
        if isinstance(data_to_save, list):
            # check if the length of the field
            # match with the length of the
            # parameter passed in
            # else, throw an Exception
            check_data = self.__check_field_length(data_to_save)
            if check_data:
                new_dict = {}
                # for item in fields
                # change field item to key
                # and asign data[index]
                # to the dict key
                for index in range(len(self.fields)):
                    new_dict[self.fields[index]] = data_to_save[index]
                self.__data_dict[str(uuid.uuid4())] = new_dict

                # increment the index
                # by 1
                self.idx += 1

                # commit the changes made to the dict
                self.__commit_additions()

                # create a logging data
                if self.modifications:
                    self.__create_message("Added data to the database")
        else:
            raise TypeError("Expected a list")

    # create info message
    # when doing actions
    def __create_message(self, data):
        print(f"INFO:{data}")

    # get the data inside of
    # the database file as json
    # or return the dict
    def __get_file_dict(self):
        with open(self.filename, "r") as json_reader:
            try:
                return json.load(json_reader)
            except Exception as exc:
                raise {}

    # get all the uuid's
    # in the data storing
    # dictioanry
    def ids(self):
        return [data_key for data_key in self.__data_dict]

    # clear all the fields
    # int the database
    # or empty the database
    def clear(self):
        # set the __data_dict to {}
        # and commit all the changes
        # to the file
        self.__data_dict = {}
        self.__commit_additions()

        if self.modifications:
            self.__create_message("Cleared the database")

    # delete a data field based
    # on the given key
    def delete(self, delete_object_key):
        if delete_object_key in self.__data_dict:
            del self.__data_dict[delete_object_key]
            self.__commit_additions()

            if self.modifications:
                self.__create_message("Deleted data from database")
        else:
            raise KeyError(f"Cannot find object with id {delete_object_key}")

    def set_track_modification(self, new_modify_value):
        if isinstance(new_modify_value, bool):
            self.modifications = new_modify_value
        else:
            raise TypeError("Expected a boolean value")

    # change a specific value
    # from the database
    def change(self, id, identifier, data):
        self.__data_dict[id][identifier] = data
        self.__commit_additions()

        if self.modifications:
            self.__create_message("Changed data in the database")

    # filter out objects
    # from the database dict based
    # on the parameters
    # passed in
    def filter(self, matches):
        # make sure that the
        # parameter is a dict
        # else, throw a TypeError
        if isinstance(matches, dict):
            # check if the length
            # of the matches is equsl
            # to the length of the
            # fields
            data = self.__check_dict_length(matches)
            if data:
                fields = []
                for el in matches:
                    # append to the fields if it
                    # equal to the entered data
                    fields.append(self.__get_key_match(el, matches[el]))

                # return all duplicate items
                # from the fields
                return self.__remove_dup(fields)
        else:
            raise TypeError("Expected a dict")

    # return duplicat items
    def __remove_dup(self, fields):
        all_keys = []
        # take each element of
        # the first fields array and
        # make sure it is also present in
        # in the other array
        # if True:append to the final array
        for el in fields[0]:
            if self.__has_in_all(el, fields):
                all_keys.append(el)
        return all_keys

    # check if an element is present
    # in given array
    def __has_in_all(self, el, fi):
        # for element in
        # fields
        # if el not present in one field
        # return false
        for k_fi in fi:
            if el in k_fi:
                pass
            else:
                return False
        return True

    # check whether it is same
    # as in the dictionary
    def __get_key_match(self, key, value):
        data = []
        for el in self.__data_dict:
            if self.__data_dict[el][key] == value:
                data.append(el)
        return data

    # get the object with a specific id
    def get(self, key):
        if key in self.__data_dict:
            return self.__data_dict[key]
        else:
            return {}

    # check whether the size
    # of the dict match with the matches
    def __check_dict_length(self, match):
        # loop through each element
        # in the dictionary and
        # make sure that the element
        # is present in the fields
        # else , raise a KeyError
        for el in match:
            if el not in self.fields:
                raise KeyError(f"Cannot find key {el}")
        return True

    # this is a secret function
    def get_dict_all_data_values_as_dict(self):
        return self.__data_dict

    # check whether the parameter
    # length is equal to the
    # self.fields length
    # else raise an error
    def __check_field_length(self, data):
        if len(data) == len(self.fields):
            return True
        else:
            raise Exception(
                f"Expected length {len(self.fields)} but got {len(data)}")
