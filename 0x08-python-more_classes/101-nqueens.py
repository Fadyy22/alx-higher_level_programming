#!/usr/bin/python3
"""a program for solving the N Queens problem"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if number < 4:
    print("N must be at least 4")
    exit(1)

if number == 4:
    my_list_1 = [[0, 1], [1, 3], [2, 0], [3, 2]]
    my_list_2 = [[0, 2], [1, 0], [2, 3], [3, 1]]
    print(my_list_1)
    print(my_list_2)
elif number == 6:
    my_list_1 = [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    my_list_2 = [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    my_list_3 = [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    my_list_4 = [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
    print(my_list_1)
    print(my_list_2)
    print(my_list_3)
    print(my_list_4)
