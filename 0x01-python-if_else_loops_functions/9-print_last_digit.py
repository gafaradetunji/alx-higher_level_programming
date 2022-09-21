#!/usr/bin/python3
def print_last_digit(number):
    num = int(input())
    digit = num % 10
    print("{} {}".format(num, digit), end=', ')
