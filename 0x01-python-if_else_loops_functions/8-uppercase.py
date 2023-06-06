#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            char = chr(ord(i) - 32)
        else:
            char = i
        print("{}".format(char), end='')
    print("{}".format(''))
