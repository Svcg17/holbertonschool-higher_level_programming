#!/usr/bin/python3
def roman_to_int(roman_string):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        if (roman_string) or (isinstance(roman_string, str)):
            for i in range(len(roman_string)):
                if i + 1 >= len(roman_string):
                    total += rom[roman_string[i]]
                    break
                if rom[roman_string[i]] < rom[roman_string[i + 1]]:
                    total -= rom[roman_string[i]]
                else:
                    total += rom[roman_string[i]]
            return total
        else:
            return 0
