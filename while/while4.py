""" Crie um programa em Python que solicite ao usuário que digite números inteiros. O programa só deve parar quando for digitado -1. Ao final, mostre:
-Quantos números foram digitados?
-Qual a soma entre eles?"""

numero = 0 
soma = 0
quant = 0

while numero != -1:
    quant += 1
    soma += numero
    numero = int(input("Digite um número inteiro: "))
    if numero == -1:
        quant += -1
        break
print("A soma dos número digitados vale: ", soma)
print("A quantidade de número digitados foi: ", quant)