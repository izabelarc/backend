# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = list(range(1, 25, 5))
soma = 0
produto = 1

for num in vetor:
    soma += num
    produto *= num

print(f"A soma dos números é: {soma}")
print(f"A multiplicação dos números é: {produto}")
print(f"Os números são: {vetor}")