#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    counter = 0
    for argument in sys.argv:
        if counter != 0:
            sum = sum + int(argument)
        counter += 1
    print("{}".format(sum))
