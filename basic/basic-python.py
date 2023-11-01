# Tratamento de strings

name = "felipe siqueira"

# todas as letras maiusculas
# print(name.upper())

# todas as letras minusculas
# print(name.lower())

# somente as primeiras letras maiusculas
# print(name.title())

# verifica se o texto está todo em maiusculo
# print(name.isupper())

# verifica se o texto está todo em minusculo
# print(name.islower())

# verifica se o texto está com as primeiras letras em maiusculo
# print(name.istitle())

# pegar parte de uma string, os parametros dentro dos colchetes são start:length
# print(name[0:8])

# pegar a última string de um texto
# print(name[-1])

# pegar a partir de uma posição da string até a última
# print(name[2: ])

# pegar o tamanho da string
# print(len(name))

number1 = 10
number2 = 3

# maior número
# print(max(number1, number2))

# menor número
# print(min(number1, number2))

# arredondamento
# print(round(0.5123, 2))

# capturar dados pelo terminal
# firstName = input('Qual o o seu primeiro nome? ')
# print(firstName)

# calculadora de juros compostos
# formula: montante = valor inicial * (1 + taxa ) ** tempo

# initialValue = float(input('Qual o valor inicial? '))
# tax = float(input('Qual a taxa? '))
# time = float(input('Em quantos meses? '))

# value = initialValue * (1 + tax) ** time
# print(f'o montante dos juros compostos é: R$ {round(value, 2)}')

banks = ['Itau', 'Bradesco', 'Banco do Brasil']
# # adicionar item ao final lista (array)
# print(banks)
# banks.append('Santander')
# print(banks)

# # adicionar item numa posição especifica
# banks.insert(2, "Nubank")
# print(banks)

# # remover um item da lista
# banks.remove("Banco do Brasil")
# print(banks)

# estruturas condicionais
# age = int(input("Digite sua idade: "))

# if age >= 18:
#   print("Maior que 18 anos")
# elif age > 10 and age < 17:
#   print("Idade entre 10 e 17 anos")
# else:
#   print("Menor de 10 anos")

# laço de repetição "for"
# for bank in banks:
#   print(bank)

# como pegar o index para usar em um for
for i in range(0, len(banks)):
  print(i)