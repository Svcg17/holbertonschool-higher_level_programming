#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i, value in enumerate(str):
        if i != n:
            newstr += value
    return newstr
