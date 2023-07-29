'''Crie uma função que recebe uma lista via parametro, em seguida sorteia cinco numeros aleatorios 
(entre 1 e 10) e preenche esta lista com os números sorteados. 
Crie também outra função que recebe uma lista via parametro e retorne a soma de todos os números pares desta lista'''

import random

def preenche(l):
    while len(l) < 5:
        aleatorio = random.randint(1,10)
        if aleatorio not in l:
            l.append(aleatorio)

lista_real = [4, 5]

preenche(lista_real)

print(F"Os elementos da lista são: {lista_real}")

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

total = soma_pares(lista_real)

print(f"A soma dos números pares é: {total}")