'''
Crie um programa que leia o nome de uma pessoa e diga
se ela tem "SILVA" no nome.
DICA - achar o true ou false

Esse programa diferente do anterior quer encontrar
o nome silva independente da posição.
'''

'''Travei na parte mais simples, era só ter colocado o nome em upper ou lower
e depois da variável nome colocar .upper() ou .lower().
Lembrando que in é um operador.'''
'''nome = str(input('Digite seu nome completo: ')).strip()
busca = 'SILVA' in nome.upper()
print(nome)
print('Seu nome tem Silva!', busca)
'''

#Guanabara fez da seguinte forma

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva ? {}'.format('silva' in nome.lower()))