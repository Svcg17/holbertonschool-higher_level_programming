#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            i = (ord(i) - 32)
            print("{}".format(chr(i)), end="")
        else:
            print("{}".format(i), end="")
    print()
