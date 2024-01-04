#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        print("{} {} {} = {}".format(a, operator, b, result))
