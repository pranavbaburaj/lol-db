
# the lol arrys
# the speciality of lol
# arrays is that
# they are typed and do not
# support duplicate elements
import math
import random

class Array():
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

    def element_at(self, index):
        # get the array element
        # at the specified index
        return self.__array_members[index]

    # get the median of the
    # array
    def median(self):
        """
        Get the median of the array
        => [1, 2, 3] => 
            i : floor(len(arr) / 2)
            -> arr[i]
        => [1, 2, 3, 4] =>
            i : floor(len(arr) / 2)
            -> ( arr[i] + arr[i - 1] ) / 2
        """
        if self.typeof == int or self.typeof == float:
            """
            if the length of the array
            is even get the sum of the 
            two numbers at the middle

            if the length of the array
            is odd get the number at the middle
            """
            if len(self.__array_members) % 2 == 0:
                arr_split_index = math.floor(self.len() / 2)
                return (self.__array_members[arr_split_index] + self.__array_members[arr_split_index - 1]) / 2
            else:
                return self.__array_members[
                    math.floor(self.len() / 2)
                ]

        else:
            raise Exception("elements should be numbers")

    # search insert position
    def search_inser_position(self, target_number):
        """
        Search insert position
        ----------------------
        => if element exists in arr return the
        index
        => else return the index if the element
        has to be appended to a sorted array
        """
        if target_number not in self.__array_members:
            self.add(target_number)

        return self.__array_members.index(target_number)

    # return the indexes
    def index(self, find_element):
        """
        Loop through all elements in
        the list and append to
        the index array
        if they find an element that match's
        the parameter
        """
        all_arr_indexes = []
        for index, element in enumerate(self.__array_members):
            if element == find_element:
                all_arr_indexes.append(index)

        return all_arr_indexes
        

    # return the first appearance 
    def first(self, find_element):
        arr = self.index(find_element)
        if len(arr) is not 0:
            return arr[0]
        
    # get the index of
    # the largest number in
    # the list
    def peak_index(self):
        return self.__array_members.index(
            max(self.all())
        )

    # get the count of the number
    # of times an element 
    # appears in the 
    # array
    def count(self, target_element):
        return len(self.index(target_element))

    # sort the array in ascending order
    def sort(self):
        self.__array_members.sort()
        return self.__array_members

    def find(self, d_t_f):
        indexes = []
        for x in range(len(self.__array_members)):
            if self.__array_members[x] == d_t_f:
                indexes.append(x)

        return indexes

    # clear the array
    def clear(self):
        self.__array_members = []
        return self.__array_members

    # reverse the array
    def reverse(self):
        self.__array_members.reverse()
        return self.__array_members

    # returns a multi-dimensional array
    # containing elements
    # at the alternate indexes
    def alternate_indexes(self):
        v_a_r = [[],[]]
        for x in range(len(self.__array_members)):
            if x % 2 == 0:
                v_a_r[0].append(x)
            else:
                v_a_r[-1].append(x)

        return v_a_r

    # return a random 
    # element from
    # the array
    def choice(self): 
        """
        Returns a randome element from the array
        """
        return self.__array_members[
            random.randint(
                0,
                self.len()
            )
            ]

    def front(self):
        if len(self.__array_members) is not 0:
            return self.__array_members[0]

    def back(self):
        if len(self.__array_members) is not 0:
            return self.__array_members[-1]

    def range(self, range):
        if range == "max":
            return max(self.__array_members)
        elif range == "min":
            return min(self.__array_members)
        else:
            raise Exception("Range should be max or min")

    def empty(self):
        return len(self.__array_members) == 0

    # extend the array size
    def extend(self, new_size):
        # if the length is not specified
        # or the length == NOne
        # check if the new_size is
        # greater than the old size
        # if yes asign the new value
        # to self.lengthog
        # else, throw an error
        if self.lengthof is not None:
            if new_size > self.lengthof:
                self.lengthof = new_size
            else:
                raise Exception("The new size should be greater than the current size")
        else:
            raise Exception("Cannot change the None to length")







