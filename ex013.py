# Leia o salário atual e mostre o aumento com 15% de aumento?
print('Calculadora de aumento salarial!')
salario = float(input('Digite seu salário: '))
aumento = 15/100
valor_aumento = salario * aumento
final = salario + valor_aumento
print('Você teve um aumento de {0}%, que representa R${1} reais e o valor total é de R${2} reais.'.format(aumento, valor_aumento, final))

#Minha maior dificuldade nos exercícios 12 e 13 foi entender a lógica de como realizar os cálculos de %.
#Sintaxe do python ok, usar o .format() também compreendi, definir o tipo da variável ok.
#O mais difícil foi a parte matemática porque tenho uma base ruim de matemática.