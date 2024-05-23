n = input('Digite algo: ') #Sempre o input é um str, por isso a necessidade de converter o tipo
print('O tipo primitivo desse valor é:',type(n))
print('Tem apenas espaços?',n.isspace())
print('É um número?',n.isnumeric())
print('É alfabético?',n.isalpha())
print('É alfanumérico?',n.isalnum())
print('Está em maiúsculas?',n.isupper())
print('Está em minúsculas?',n.islower())
print('Está capitalizada?',n.istitle())
