# Mostre a largura e altura de uma parede em metros
# Calcule a area e a quantidade de tinta necessária para pintar sabendo que cada litro de tinta
# pinta uma área de 2m²
print('Olá, seja bem-vindo ao nosso site!')
lag = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = lag * alt
tinta = area/2
print('Para pintar o espaço informado medindo {0}m de altura por {1}m de largura,\nvocê irá precisar de {2}L de tinta.'.format(lag, alt, tinta))
