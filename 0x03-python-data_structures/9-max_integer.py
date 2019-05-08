#!/usr/bin/python3
def max_integer(my_list=[]):
        if my_list:
            maxval = my_list[0]
            for i in my_list:
                if i >= maxval:
                    maxval = i
            return maxval
        else:
            return None
