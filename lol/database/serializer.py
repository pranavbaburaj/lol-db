import json
from lol.database.database import Database
import dicttoxml


class DatabaseSerializer():
    def __init__(self, database_object):
        # the main database object
        # which contains the filename
        # and is converted to json data
        self.database = database_object

    # convert the database
    # values (in dict) to
    # json form
    def jsonify(self):
        return json.dumps(self.database.get_dict_all_data_values_as_dict(),
                          indent=6)

    # convert the database
    # values(int dict) to
    # xml form
    def xml(self):
        return dicttoxml.dicttoxml(
            self.database.get_dict_all_data_values_as_dict())
