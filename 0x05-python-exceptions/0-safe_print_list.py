#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
            counter = 0
            for elem in my_list:
                if elem in range(0, x + 1):
                    try:
                        print("{}".format(elem), end="")
                        counter += 1
                    except:
                        print(None)
            print()
            return counter
