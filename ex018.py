"""
Ex018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

Exercício complexo, eu consegui fazer até certo ponto, porém não sabia que deveria aninhar as funções com radians.
"""

from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo que deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno de {} é {:.2f}.'.format(ang, sen))
print('O cosseno de {} é {:.2f}.'.format(ang, cos))
print('A tangente de {} é {:.2f}.'.format(ang, tan))
