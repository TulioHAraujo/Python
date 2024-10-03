'''
Faça um programa que leia uma frase pelo teclado e mostre:
1- Quantas vezes aparece a letra "A".
2- Em que posição ela aparece a primeira vez.
2- Em que posição ela aparece a última vez.

Não consegui remover o espaço em branco no meio da string.
Optei por converter para lower(), mas poderia usar upper().
'''

'''
Minha solução:
text = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes na frase.'.format(text.lower().count('a'.lower())))
print('A letra "a" aparece a primeira vez na posição {}.'.format(text.lower().find('a'.lower())))
print('A letra "a" aparece pela última vez na posição {}.'.format(text.lower().rfind('a'.lower())))
'''

#Solução do Guanabara:
'''frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
'''

#Melhorando meu código
text = str(input('Digite uma frase: ')).lower().strip()
print('A letra "a" aparece {} vezes na frase.'.format(text.count('a')))
print('A letra "a" aparece a primeira vez na posição {}.'.format(text.find('a')+1))
print('A letra "a" aparece pela última vez na posição {}.'.format(text.rfind('a')+1))