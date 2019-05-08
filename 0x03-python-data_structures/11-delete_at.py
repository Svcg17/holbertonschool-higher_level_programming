#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            for i in range(0, len(my_list)):
                if idx == i:
                    del my_list[idx]
                    return my_list
