#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(char_code), end="")
for char_code in range(ord('Z'), ord('A') - 1, -1):
    print("{:c}".format(char_code), end="")
print()
