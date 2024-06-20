"""
Ex019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido.
import random.

Vale lembrar que até o momento nas aulas não haviamos visto nenhum conteúdo sobre listas

Basicamente eu fiz errado o exercício, abaixo o código que eu criei sozinho:

import random

print('Sorteio para apagar o quadro!')
print('Participantes e seu número no sorteio: João 1, Carla 2, Pedro 3 e Maria 4.')
num = random.randint(1, 4)
print('O número sorteado foi {}'.format(num))
"""

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

res = choice(lista)
print('O aluno escolhido é {}.'.format(res))
