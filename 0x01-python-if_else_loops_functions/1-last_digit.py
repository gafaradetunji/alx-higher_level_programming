#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number  % 10

print(f"Last digit of {digit} is {number}")
if digit > 5:
    print(f"and is greater than 5")
elif digit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0\n")