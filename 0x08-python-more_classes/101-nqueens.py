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
