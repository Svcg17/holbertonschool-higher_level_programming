#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leni = len(argv) - 1
    j = 1
    if leni == 0:
            print("{} arguments.".format(leni))
    elif leni == 1:
        print("{} argument:".format(leni))
    else:
        print("{} arguments:".format(leni))
    while leni >= j:
        print("{}: {:s}".format(j, argv[j]))
        j = j + 1
