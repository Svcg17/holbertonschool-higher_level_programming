#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}\n".format(value), end="")
        return True
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
