#!/usr/bin/python3
for i in range(1, 100):
    if i == 89:
        print(f"{i:d}")
        break
    if (i / 10) > (i % 10):
        continue
    print(f"{i:02d}, ", end='')
