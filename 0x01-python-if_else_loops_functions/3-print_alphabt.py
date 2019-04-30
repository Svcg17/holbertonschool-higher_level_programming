#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 113 or letter == 101:
        continue
    else:
        print(chr(letter), end="")
