# Aplique desconto de 5% em um produto?
"""print('Olá, seja bem-vindo ao nosso site!')
prod = float(input('Digite o preço do produto: R$'))
desc = 5 / 100 # Aqui eu calculo o valor do desconto
valor_desc = prod * desc # Aqui eu mostro o valor do desconto em reais ex: você teve um desconto de 15 reais.
final = prod - valor_desc #Aqui é o valor cheio do produto já com desconto aplicado
print('O produto selecionado teve um desconto de {2}%, você economizou R${0} reais,\n o produto irá custar R${1} reais!'.format(valor_desc, final, desc))
"""
#Depois de muito pesquisar consegui
#Basicamente é necessário realizar uma divisão da porcentagem do desconto por 100
#Multiplicar o valor inserido pelo usuário pelo resultado da divisão da porcentagem
#E subtrair o valor do usuário pelo valor do desconto. Não é tão simples

"""O meu código deu certo acima, porém existe uma forma mais fácil"""
preco = float(input('Qual o preço do produto? R$'))
novop = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto, sai por apenas R${:.2f}.'.format(preco, novop))
