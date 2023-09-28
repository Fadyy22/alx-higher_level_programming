#!/usr/bin/python3
"""module containing peak() function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if list_of_integers:
        for i in range(len(list_of_integers)):
            if i == 0:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]
            elif i == len(list_of_integers) - 1:
                if list_of_integers[i] >= list_of_integers[i - 1]:
                    return list_of_integers[i]
            else:
                if (
                    list_of_integers[i] >= list_of_integers[i + 1]
                    and list_of_integers[i] >= list_of_integers[i - 1]
                ):
                    return list_of_integers[i]
    else:
        return None


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
