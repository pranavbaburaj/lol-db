import string

# string data types
# strings are groups
# of characters


class String():
    def __init__(self, string_object):
        # the main string
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
                raise Exception(
                    f"Expected a character, but string of length {len(throw_away_object)} found"
                )
        else:
            raise TypeError("Expected a string")

    # get the character
    # at the specified index
    def character_at(self, index):
        if self.length() > index:
            return self.__string[index]
        else:
            raise Exception("Index out of range")

    # replace a specific character
    # by annother word
    def replace(self, exists, new):
        # Create a new string
        # check whether both parameters
        # are strings

        # if yes loop through each element in
        # the list and if the find the existsing
        # string replace it with the new one

        # and return the new_string

        new_string = ""
        if isinstance(exists, str) and isinstance(new, str):
            for element in self.__string:
                if element == exists:
                    new_string += new
                else:
                    new_string += element
        else:
            raise TypeError("Arguments expected to be strings")
        return new_string

    # return the string in the form
    # of a list
    def each(self):
        return list(self.__string)

    # check for startswi5th or endswith
    def starts_with(self, element):
        if self.__string == "":
            return False
        else:
            return self.__string[0] == element

    def ends_with(self, element):
        if self.__string == "":
            return False
        else:
            return self.__string[-1] == element

    # remove all the spaces
    # from the string
    def remove_spaces(self):
        # create a new string
        # loop through each element
        # of the string
        # if the string is not a space
        # add it to the
        # new string
        new_string = ""
        for element in self.__string:
            if element is not " ":
                new_string += element
        return new_string

    # get the number of times
    # a character appears
    # int the string

    def count(self, target):
        # loop through each
        # element in the
        # string and if the character
        # matched the target
        # increment the target_count

        target_count = 0

        if len(target) == 1:
            for el in self.__string:
                if el == target:
                    target_count += 1
            return target_count
        else:
            raise Exception(
                f"Expected a character, but string of length {len(target)} found"
            )

    # get the index of the character
    def index(self, character):
        # if the length of the
        # string is 1 return
        # the index of the specified
        # element in the
        # string
        character = str(character)
        if len(character) == 1:
            return self.__string.index(character)
        else:
            raise Exception(
                f"Expected a character, but string of length {len(character)} found"
            )

    # the repr function
    # is added inorder to
    # return the private
    # string when calling the object

    # example => print(<string-object>)
    def __repr__(self):
        return self.__string