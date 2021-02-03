# the lol arrys
# the speciality of lol
# arrays is that
# they are typed and do not
# support duplicate elements


class LOLArray():
    def __init__(self, typeof_array, length=None):
        # the type of the
        # elements in the array

        self.typeof = typeof_array

        # array members
        # this variable is private 
        # the user can only access
        # this via self.all()
        # function

        self.__array_members = []
        self.lengthof = length

    def all(self):
        # return all the members of
        # the array list
        return self.__array_members

    def add(self, data):
        if self.lengthof is not None:
        
            if len(self.__array_members) == self.lengthof:
                raise Exception("Array size limit exceeded")

        if type(data) == self.typeof:
            if data not in self.__array_members:
                self.__array_members.append(data)
        else:
            raise TypeError("Type don't match")
