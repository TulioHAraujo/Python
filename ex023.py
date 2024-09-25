'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
separados.
Ex: Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

Tentar fazer como string ou matematicamente.
'''

'''Fiz está parte sem auxílio
n = str(input('Digite um número: '))
nu = n[3]
nd = n[2]
nc = n[1]
nm = n[0]
print('O número {} é uma unidade de milhar.'.format(nm))
print('O número {} é uma centena.'.format(nc))
print('O número {} é uma dezena.'.format(nd))
print('O número {} é uma unidade.'.format(nu))'''

'''
Esbarrei em um problema, da forma que eu fiz cheguei no mesmo 
resultado que o Guanabara, porém se eu não utilizo os 4 digitos 
surge um erro. (E o outro problema é que até esse momento do curso
não vimos estrutura de condição/repetição, então "não tenho" como
fazer com que caso um dos dígitos não seja preenchido pelo usuário
o resultado ai traga algo no print).
'''

#Forma matemática de fazer segundo o Guanabara
#Trata-se de uma solução matemática, precisa ter um nível mais complexo de conhecimento.
num = int(input('Informe um número: '))
u = num // 1 % 10 #dividindo o número e pegando o resto da divisão inteira
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))