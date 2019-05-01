#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            i = (ord(i) - 32)
            print("{:s}".format(chr(i)), end="")
        else:
            print("{:s}".format(i), end="")
    print()
