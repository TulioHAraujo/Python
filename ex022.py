'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas.
2- O nome com todas as letras minúsculas.
3- Quantas letras ao todo (sem considerar espaços). atenção retirar espaços internos
4- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: '))
up = str.upper(nome)
lw = str.lower(nome)
total_letras = len(nome.replace(" ","")) #O método len lê todos os caracteres, o replace substitui os espaços em branco, dessa forma ajuda a ler somente as letras
""" Esse é o frankstein que eu criei
qt = nome.split() # essa parte não sei fazer
res = qt[0]
pnome = len(res)"""
pnome = len(nome.split()[0])

#print(up,"\n",lw,"\n",total_letras,pnome)
print("""Seu nome em letras maiúsculas é: {0}.
Seu nome em letras minúsculas é: {1}.
Seu nome possui {2} letras.
Seu primeiro nome tem {3} letras.""".format(up, lw, total_letras,pnome))

"""Achei um pouco complicado resolver esse exercício, porém nada muito absurdo, dificuldade maior com sintaxe"""