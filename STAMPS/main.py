# coding: utf-8

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (int(i) for i in stdin.read().split())
escenarios = next(entrada)

for i in range(escenarios):
    estampas = next(entrada)
    amigos = next(entrada)
    lista = []
    for j in range(amigos):
        lista.append(next(entrada))
    lista.sort(reverse=True)
    n = 0
    suma = 0
    while n < len(lista) and suma < estampas:
        suma += lista[n]
        n += 1
    print('Scenario #{0}:'.format(i + 1))
    if suma < estampas:
        print('impossible')
    else:
        print(n)
    print()
