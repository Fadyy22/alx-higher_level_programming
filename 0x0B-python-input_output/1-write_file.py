#!/usr/bin/python3

"""module containing write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        no_chars = f.write(text)
    return no_chars
