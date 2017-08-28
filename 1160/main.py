# coding: utf-8

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (int(i) for i in stdin.read().split())

N = next(entrada)
for i in range(N):
    x = next(entrada)
    y = next(entrada)
    if x == y or y == x - 2:
        v = 2 * x
        if x % 2 == 1:
            v -= 1
        if x != y:
            v -= 2
        print(v)    
    else:
        print('No Number')


