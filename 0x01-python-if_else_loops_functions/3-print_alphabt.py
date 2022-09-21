#!/usr/bin/python3
letters = range(97,123)
for c in letters:
    if chr(c) is not 'e' and chr(c) is not 'q':
        print("{}".format(chr(c)), end=' ')
