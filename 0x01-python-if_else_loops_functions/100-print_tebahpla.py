#!/usr/bin/python3
for letra in range(122, 96, -1):
    if letra % 2 == 0:
        print("{:s}".format(chr(letra)), end="")
    else:
        print("{:s}".format(chr(letra - 32)), end="")
