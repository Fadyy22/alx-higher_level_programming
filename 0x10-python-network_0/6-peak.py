#!/usr/bin/python3
"""module containing peak() function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    li = list_of_integers

    if li == []:
        return None

    left = 0
    right = len(li) - 1

    while left <= right:
        if li[left] >= li[left + 1]:
            return li[left]
        if li[right] >= li[right - 1]:
            return li[right]
        left += 1
        right -= 1


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
