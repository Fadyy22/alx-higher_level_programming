#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print(f"{ord(i) - 32:c}" if 97 <= ord(i) <= 122 else f"{i}", end='')
    print()
