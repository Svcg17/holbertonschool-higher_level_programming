#!/usr/bin/python3
def no_c(my_string):
        new = ""
        if my_string:
            for i in range(0, len(my_string)):
                if (my_string[i] != 'C') & (my_string[i] != 'c'):
                    new += my_string[i]
            return new
