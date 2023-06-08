#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif sys.argv[2] == '-':
        result = sub(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif sys.argv[2] == '*':
        result = mul(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif sys.argv[2] == '/':
        result = div(a, b)
        print("{} + {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
