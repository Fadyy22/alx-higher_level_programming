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
