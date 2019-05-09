#!/usr/bin/python3
def search_replace(my_list, search, replace):
        new = []
        if my_list:
            new = my_list.copy()
            for i, elem in enumerate(new):
                if elem == search:
                    new[i] = replace
            return new
