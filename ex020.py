"""
Ex020
O professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
Esse é um pouquinho mais dificil.

Ex021
Faça um programa que abra e reproduza um áudio de um arquivo mp3.
Difícil.
"""

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

sorteio = choice(lista)
res = sorted(sorteio)
print(res)
