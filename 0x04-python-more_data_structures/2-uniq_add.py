#!/usr/bin/python3
def uniq_add(my_list=[]):
        if my_list:
            suma = 0
            sett = set(my_list)
            new = list(sett)
            for i in new:
                suma += int(i)
            return suma
