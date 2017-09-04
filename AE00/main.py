# coding: utf-8

from __future__ import print_function
from __future__ import division

from sys import stdin
from math import sqrt

N = int(stdin.read())

suma = 0
for i in range(1, int(sqrt(N)) + 1):
    suma += N // i - i + 1
print(suma)
