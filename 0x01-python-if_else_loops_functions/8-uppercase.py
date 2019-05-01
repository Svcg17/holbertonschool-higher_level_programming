#!/usr/bin/python3
def uppercase(str):
    strig = ""
    for i in str:
        if (ord(i) in range(97, 123)):
            strig += chr(ord(i) - 32)
        else:
            strig += i
    print("{:s}".format(strig))
