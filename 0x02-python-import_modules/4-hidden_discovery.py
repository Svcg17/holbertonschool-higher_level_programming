#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for i in dir():
        if i[:2] != "__":
            print("{:s}".format(i))
