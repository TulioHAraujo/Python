# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros?
m = float(input('Digite o valor em metros (ex: 1.2, 1.80): '))
cm = m * 100 #para converter em centímetros você múltiplica por 100
mm = m * 1000 # múltiplica por 1000
km = m % 1000
print('O valor em metros é {0}m, em centímetros {1}cm e em milímetros {2}mm. Em {3}km'.format(m, cm, mm, km))
