#!/usr/bin/python3
"""

a module containing a text_indentation function

"""


def text_indentation(text):
    """a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): text to perform indentation on

    Raises:
        TypeError: if text is not a string
    """
    new_text = ""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if i == len(text) - 1:
            new_text += text[i]
        elif text[i] in (".", "?", ":"):
            new_text += text[i]
            new_text += "\n\n"
        elif text[i] == " " and text[i - 1] in (".", "?", ":"):
            continue
        else:
            new_text += text[i]
    print(new_text, end="")
