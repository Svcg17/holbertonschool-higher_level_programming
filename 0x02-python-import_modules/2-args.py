#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leni = len(argv) - 1
    if leni == 0:
            print("{} arguments.".format(leni))
    elif leni == 1:
        print("{} argument:".format(leni))
    else:
        print("{} arguments:".format(leni))
    for i in range(1, len(argv)):
        print("{}: {:s}".format(i, argv[i]))
