"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
EX: Digite um número: 6.127.
O número 6.127 tem a parte inteira 6.
Dica: olhar a biblioteca math

Respota:
from math import trunc

num = float(input('Digite um número: '))
res = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, res))

Lembrando que posso criar sem declarar a variável:
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}').format(num, trunc(num)))

E também é possível fazer de uma maneira mais simples:
"""
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
