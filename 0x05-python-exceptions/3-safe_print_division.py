#!/usr/bin/python3
from decimal import DivisionByZero


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except DivisionByZero:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
