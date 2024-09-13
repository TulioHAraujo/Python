"""
Ex020
O professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
Esse é um pouquinho mais dificil.
"""

from random import sample

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

sorteio = sample([a1,a2,a3, a4], counts=[1, 1, 1, 1], k=4)

print('A ordem se apresentação será: ')
print(sorteio)

"""
Resolução do exercício (eu não utilizei shuffle porque não entendi a sintaxe)
Mas consegui chegar no mesmo resultado kkkk

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1. n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)"""