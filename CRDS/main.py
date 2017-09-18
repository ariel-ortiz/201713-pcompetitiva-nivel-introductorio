# coding: utf-8

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (int(x) for x in stdin.read().split())
T = next(entrada)
for i in range(T):
    N = next(entrada)
    r = ((3 * N * (N + 1)) // 2 - N) % 1000007
    print(r)
