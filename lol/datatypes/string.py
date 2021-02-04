import string

# string data types
# strings are groups
# of characters

class String():
    def __init__(self, string_object):
        self.__string = str(string_object)

    # get the length of the 
    # string
    def length(self):
        return len(self.__string)

    # check whether a specified
    # substring is present
    # int the string
    def has(self, search_sub_string):
        return str(search_sub_string) in self.__string

    # remove a specific letter from the string
    def throw(self, throw_away_object):
        # check if the parameter is a string
        # if yes:pass
        # else , raise a TypeError
        # and check the length of the string

        # if the length == 1
        # create a string and append it to
        # if the current_character is not the target
        # and return the new variable

        # else raise and Exception
        if isinstance(throw_away_object, str):
            if len(throw_away_object) == 1:
                data = ""
                for index in range(len(self.__string)):
                    current_character = self.__string[index]
                    if current_character is not throw_away_object:
                        data += current_character
                return data

            else:
                raise Exception(f"Expected a character, but string of length {len(throw_away_object)} found")
        else:
            raise TypeError("Expected a string")
    # the repr function
    # is added inorder to 
    # return the private
    # string when calling the object

    # example => print(<string-object>)
    def __repr__(self):
        return self.__string