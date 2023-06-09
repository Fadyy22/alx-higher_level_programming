#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500, 'M': 1000}
    sum = 0
    i = 0
    while i < len(roman_string):
        value = roman_numbers[roman_string[i]]
        if (i + 1) < len(roman_string):
            if value >= roman_numbers[roman_string[i + 1]]:
                sum += value
                i += 1
            else:
                sum -= value
                i += 1
        else:
            sum += value
            i += 1
    return sum
