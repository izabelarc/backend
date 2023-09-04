'''Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:

- A média de idade de todo o grupo.

- Qual o nome da pessoa mais velha.

- Quantas pessoas têm menos de 20 anos.

- Quantas pessoas têm mais de 40 anos.

- Qual o sexo da pessoa mais nova.'''

soma = 0
idade_mais_velho = 0
nome_mais_velho = ""
menos = 0
maior = 0
sexo_mais_nova = ""
idade_mais_nova = 0

for i in range(0,5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")

    soma+=idade

    if idade > idade_mais_velho:
        nome_mais_velho=nome
        idade_mais_velho=idade

    if idade < 20:
        menos += 1

    if idade > 40:
        maior += 1

    if i == 0 or idade < idade_mais_nova:
        sexo_mais_nova = sexo

media = soma/5
print("A média da idade é de: ", media)
print("A pessoa mais velha é: ", nome_mais_velho)
print("O número de pessoas com menos de 20 anos é: ", menos)
print("O número de pessoas com mais de 40 anos é: ", maior)
print("O sexo da pessoa mais nova é: ", sexo_mais_nova)
