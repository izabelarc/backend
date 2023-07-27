# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

lista = list(range(20))

impar = []
par = []

for num in lista:
    if (num % 2) == 1:
        impar.append(num)
    else:
        par.append(num)

print(lista)
print(impar)
print(par)
