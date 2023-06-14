#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    roman_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
                     'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    num = 0
    idx = 0
    length = len(roman_string)
    while idx < length:
        if (roman_string[idx: idx + 2] in roman_symbols) and idx + 1 < length:
            num += roman_symbols[roman_string[idx: idx + 2]]
            idx += 2
        else:
            num += roman_symbols[roman_string[idx]]
            idx += 1
    return num
