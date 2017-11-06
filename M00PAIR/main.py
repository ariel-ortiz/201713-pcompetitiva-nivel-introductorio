# def secuencia(lst):
#     resultado = []
#     for e in lst:
#         if e == 0:
#             resultado.extend([1, 0])
#         else:
#             resultado.extend([0, 1])
#     return resultado

# def contar_doble_ceros(lst):
#     cont = 0
#     for i in range(len(lst) - 1):
#         if lst[i] == lst[i + 1] == 0:
#             cont += 1
#     return cont

# lst = [1]
# for n in range(15):
#     lst = secuencia(lst)
#     print(n + 1, contar_doble_ceros(lst))

# f(n) = 0, n = 1
# f(n) = 2 * f(n - 1) + (-1) ** n, n > 1

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (int(x) for x in stdin.read().split())

valor = [0, 0]
signo = 1
for i in range(1000):
    valor.append(valor[-1] * 2 + signo)
    signo = -signo

for n in entrada:
    print(valor[n])

