'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome
"SANTO".
'''

'''city = str(input('Digite o nome da cidade: '))
print('Santo' in city)'''

"""Ok, de certa forma resolvi o problema com o código acima,
porém o enunciado ficou meio ruim, e provavelmente eu consigo fazer
de forma mais sofisticada usando uma condição que permita 
mostrar na tela o nome da cidade e se ela possui a palavra Santo ou não."""

#Solução do Guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

'''Achei um exercício meio mal feito kkkk'''