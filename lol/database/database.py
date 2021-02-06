import os
import json
# the main database 

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

        # index of the data
        # or id of each data fields
        self.idx = 0

        # the main dictionary in which the data
        # is going to be stored
        self.__data_dict = self.__get_file_dict()

        # create the database
        self.filename = self.__create_new_database_file(self.table)
        self.__commit_additions()


        print(self.filename)

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
        with open(filename, "w") as create_file_object:
            create_file_object.write(" ")
        
        
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
                self.__data_dict[str(self.idx)] = new_dict

                # increment the index 
                # by 1
                self.idx += 1

                # commit the changes made to the dict
                self.__commit_additions()
        else:
            raise TypeError("Expected a list")

    # get the data inside of
    # the database file as json
    # or return the dict
    def __get_file_dict(self):
        return {}

    # check whether the parameter
    # length is equal to the
    # self.fields length
    # else raise an error
    def __check_field_length(self, data):
        if len(data) == len(self.fields):
            return True
        else:
            raise Exception(f"Expected length {len(self.fields)} but got {len(data)}")