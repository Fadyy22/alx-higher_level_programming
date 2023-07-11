#!/usr/bin/python3

"""module containing append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        no_chars = f.write(text)
    return no_chars
