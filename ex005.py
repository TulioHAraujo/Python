# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor?
'''n = int(input('Digite um número: '))
n1 = n + 1
n2 = n - 1
print('O número escolhido é {0}, o próximo número é {1} e o número anterior é {2}'.format(n, n1, n2))'''

#Existe outra forma de fazer que eu não sabia
n = int(input('Digite um número: '))
print('O número escolhido é {}, o seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

'''
Importante ressaltar que, no primeiro caso eu posso utilizar quando quero guardar o valor das variáveis para
uso futuro. Já o segundo caso se aplica quando eu não preciso reutilizar esses valores.
'''