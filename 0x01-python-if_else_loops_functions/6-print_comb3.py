#!/usr/bin/python3
for num in range(90):
    if (num / 10) < (num % 10):
        if (num == 89):
            print ("{:d}".format(num))
        else:
            print("{:d}".format(num), end=", ")
