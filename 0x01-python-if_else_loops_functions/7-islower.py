#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print(f"{c} is lowercase")
        return True
    else:
        print(f"{c} is uppercase")
        return False