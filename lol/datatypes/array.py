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

    # add an element to the array
    def add(self, data):
        # check if the length specified
        # is none , if yes
        # pass else check if the size
        # limit is exceeded
        if self.lengthof is not None:
        
            if len(self.__array_members) == self.lengthof:
                raise Exception("Array size limit exceeded")

        # check the types
        if type(data) == self.typeof:
            # and append it to tha array
            # if it is not present in it
            if data not in self.__array_members:
                self.__array_members.append(data)
        else:
            raise TypeError("Type don't match")

    # remove an element from the
    # array based on
    # tyhe index specified
    def remove(self, index):
        if len(self.__array_members) > index:
            del self.__array_members[index]
            # return self.__array_members[index]
        return None

    # get the length of the array
    # an easy way for doing
    # len(<array-object>.all())
    def len(self):
        return len(self.__array_members)

