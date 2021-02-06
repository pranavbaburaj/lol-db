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

        # create the database
        self.filename = self.__create_new_database_file(self.table)

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