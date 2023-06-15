#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mul_tuple = 1
        sum_tuple = 0
        sum = 0
        for tuple in my_list:
            mul_tuple = tuple[0] * tuple[1]
            sum_tuple += mul_tuple
            mul_tuple = 0
            sum += tuple[1]
        return sum_tuple / sum
    return 0
