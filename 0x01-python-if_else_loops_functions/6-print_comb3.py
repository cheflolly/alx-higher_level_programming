#!/usr/bin/python3
for i in range(0, 9):
    for n in range(i + 1, 10):
        if i == 8:
            print("{:d}{:d}".format(i, n))
            break
        print("{:d}{:d}".format(i, n), end=", ")
