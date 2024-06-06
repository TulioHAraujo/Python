"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço  a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por km rodado.
"""
print('Olá, seja bem-vindo(a)!')
dias = int(input('Por quantos dias o carro ficou alugado? '))
dp = float(input('Quantos km foram percorridos? '))
c = dias * 60  # eu fiz de uma forma mais complexa talvez kkk
km = (dp * 0.15) + c
"""solução da aula | pago = (d * 60) + (dp * 0.15)"""
print('Você alugou o carro por {} dias e percorreu {}km.\nO valor total é de R${:.2f}.'.format(dias, dp, km))
