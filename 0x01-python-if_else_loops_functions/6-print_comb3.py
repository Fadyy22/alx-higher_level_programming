#!/usr/bin/python3
for i in range(1, 100):
    if i == 89:
        print("{}".format(i))
        break
    if (i / 10) > (i % 10):
        continue
    print("{:02d}, ".format(i), end='')
