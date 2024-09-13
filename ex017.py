"""
Ex017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.

Lembrando que para usar uma biblioteca por mais que você não domine os conceitos matemáticos é necessário
minimamente entender como usa-lá, por exemplo, para usar a função hypot que calcula o valor da hipotenusa,
precisamos entender que para calcular o valor da hipotenusa precisamos de outros dois valores
e precisamos solicitar ao usuário o input de maneira correta, informando o tipo primitivo.

resposta sem usar biblioteca/modulo
hip = (co ** 2 + ca ** 2) ** (1/2)
"""
from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hip))