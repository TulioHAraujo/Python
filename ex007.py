# Programa que leia duas notas de um aluno, calcule e mostre sua média?
aluno = str(input('Qual é o seu nome? '))
nota1 = float(input('Digite a nota da P1: '))
nota2 = float(input('Digite a nota da P2: '))
media = (nota1 + nota2) / 2
print('{0} a sua média é: {1:.1f}.'.format(aluno, media))
