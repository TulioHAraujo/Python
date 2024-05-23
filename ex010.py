# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar?
# Considere US$1,00 = 5,15BRL
real = float(input('Informe quanto você possui para saber quantos dólares você pode comprar: '))
res = real / 5.15
print('Com o valor de R${}, você pode comprar o equivalente a US$ {:.2f}.'.format(real, res))
