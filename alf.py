#!/usr/bin/python3

from itertools import product

alf = input().split()
n = int(input())
for i in product(alf, repeat=n):
    print(''.join(i))

