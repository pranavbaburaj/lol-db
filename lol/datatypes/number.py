# the number class
# the number data type
# can be integers, floats,
# doubles, longs stc


class Number():
    def __init__(self, number_value):
        # the main number value
        # integers or floats
        self.value = self.__get_value(number_value)

        # the number value
        # used instead of using
        # self.value['data']
        self.data = self.value['data']

    # get the value
    # of the number
    def __get_value(self, number):
        # check if the parameter
        # is an integer or a float
        # else try converting it
        # to a float and if an exception
        # occurs, throw out the Exception
        if isinstance(number, int) or isinstance(number, float):
            return self.__get_data_type(number)
        else:
            try:
                return self.__get_data_type(float(number))
            except Exception as number_convert_exception:
                raise number_convert_exception

    # convert the integer
    # into string form
    def string(self):
        return str(self.value['data'])

    # get the data type
    # of the value passed in
    # integer, float, double, long
    def __get_data_type(self, data):
        return {
            "data": data,  # the number
            "type": type(data),  # the type , float or long
            "negative": data < 0  # data is negative
        }

    # set or change the object value
    def set_(self, new_value):
        self.data = new_value
        self.value['data'] = new_value

        return new_value

    # fix the number
    # of decimal points
    # to the parameter
    def to_fixed(self, fix_point=0):
        # make sure the type of
        # the parameter is int
        assert isinstance(fix_point, int), "Expected an integer"
        new_string = ""  # create a new string
        points = str(self.data).split(".")  # split on (.)
        new_string += f"{str(points[0])}."  # add the first string

        # if the length is greater
        # than 1(if value have decimal)
        # loop in range of the parameter
        # of the length of the decimal point
        # is less than the fix_point add some
        # zeros(0) at the end

        # return the string
        if len(points) > 1:
            after_decimal_point = str(points[-1])
            for index in range(fix_point):
                if len(after_decimal_point) == (index + 1):
                    after_decimal_point += "0"

                new_string += after_decimal_point[index]
            return new_string
        else:
            return new_string

    # check whether the number is
    # an integer
    # via splitting the decimal
    # and verfying the
    # length
    @staticmethod
    def is_integer(number):
        return len(str(number).split(".")) == 1

    # get the value
    def get(self):
        return self.value["data"]

    def __repr__(self):
        return str(self.value["data"])