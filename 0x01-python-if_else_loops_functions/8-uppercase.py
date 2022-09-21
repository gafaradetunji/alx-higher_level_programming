#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(str) >= 65 and ord(str) <= 90:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
