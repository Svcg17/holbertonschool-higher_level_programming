#!/usr/bin/python3
def weight_average(my_list=[]):
        mult = 0
        suma = 0
        if my_list:
            for x in my_list:
                mult += x[0] * x[1]
                suma += x[1]
        return mult / suma
