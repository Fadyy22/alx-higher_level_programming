#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    success_try = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            success_try = success_try + 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return success_try
