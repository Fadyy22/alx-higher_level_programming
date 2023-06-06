#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print(f"{i - 32:c}" if i % 2 != 0 else f"{i:c}", end='')
