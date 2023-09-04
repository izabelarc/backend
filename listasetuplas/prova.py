'''Escreva um programa em Python que receba duas listas como entrada 
do usuário e retorne uma tupla contendo os elementos em comum entre as duas listas
e a soma desses elementos.'''

# Obter a primeira lista do usuário
entrada1 = input("Digite os elementos da primeira lista separados por espaços: ")
lista1 = [int(num) for num in entrada1.split()]

# Obter a segunda lista do usuário
entrada2 = input("Digite os elementos da segunda lista separados por espaços: ")
lista2 = [int(num) for num in entrada2.split()]

# Obter elementos em comum
comum = [elemento for elemento in lista1 if elemento in lista2]

# Soma dos elementos em comum
soma = sum(comum)

# Resultao
print(f"({comum}{soma})")