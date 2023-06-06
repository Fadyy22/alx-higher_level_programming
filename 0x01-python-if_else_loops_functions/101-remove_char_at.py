#!/usr/bin/python3
def remove_char_at(str, n):
    if (len(str) - 1 < n or n < 0):
        return str

    str_copy = ""
    for char in str:
        if (char == str[n]):
            continue
        else:
            str_copy += char
    return str_copy
