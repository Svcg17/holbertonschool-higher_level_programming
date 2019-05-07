#!/usr/bin/python3
def no_c(my_string):
        new = ""
        if my_string:
            for i, j in enumerate(my_string):
                if (j != 'C') & (j != 'c'):
                    new += j
            return new
