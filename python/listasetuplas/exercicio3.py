'''Faça um programa que leia 10 números inteiros e separe os mesmos em 2 listas, sendo:
- 1 lista números PARES
- 1 lista números IMPARES
- Imprimir as duas listas'''
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número para entrar na lista: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
print(f"Lista de números pares: {pares}")
print(f"Lista de números ímpares: {impares}")

