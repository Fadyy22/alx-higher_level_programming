#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = {0}
    sum = 0
    for element in my_list:
        my_set.add(element)
    for element in my_set:
        sum += element
    return sum
