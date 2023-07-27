# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do
# vetor.

vetor_a = list(range(1,101, 10))
soma = 0

for num in vetor_a:
    quadrado = num * num
    soma += quadrado

print(f"A soma dos quadrados dos elementos é: {soma}")