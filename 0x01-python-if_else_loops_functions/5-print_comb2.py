#!/usr/bin/python3
for num in range(100):
    if num <= 98:
        print("{:02}, ".format(num),end="")
    else:
        print("{:02} ".format(num),end="\n")
