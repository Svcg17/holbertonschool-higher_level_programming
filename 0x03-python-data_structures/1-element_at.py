#!/usr/bin/python3
def element_at(my_list, idx):
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        elif idx == 0:
            return my_list[0]
        else:
            for i in my_list:
                if i == idx:
                    return my_list[i]
