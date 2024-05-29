# Escreva um programa que converta uma temperatura digitada em ºc e converta para ºF.
"""Sabendo que 0º celsius é o equivalente a 32ºF"""
g = float(input('Digite a temperatura em ºC: '))
#f = (g*9/5) + 32 nesse caso o parênteses não influência a ordem de precedência
print('A temperatura de {}ºC é equivalente a {}ºF.'.format(g, g * 9 / 5 + 32))
