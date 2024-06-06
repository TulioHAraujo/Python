# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada? 4**(1/2)
"""n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n **(1/2)
print('O número digitado foi {0}, o dobro é {1}, o triplo é {2} e \na raiz é {3:.3f}'.format(n, dobro, triplo, raiz))
"""

#Outra forma é não criar variáveis
n = int(input('Digite um número: '))
print('O número digitado é {} e o dobro é {}.'.format(n, (n * 2)))
print('O triplo é {} e a raiz quadrada é {:.3f}.'.format((n * 3), pow(n, (1 / 2))))

#pow() é uma função p/ calcular raiz ou (n**(1/2))
