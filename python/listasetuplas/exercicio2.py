'''Crie uma lista com 10 números inteiros á sua escolha, em seguida percorra esta lista e exiba. 
-A soma de todos os números
-O maior número
-O menor número'''

numbers = [300, 90, 43, 2, 230, 115, 170, 342, 257, 289]

soma = sum(numbers)
maior = max(numbers)
menor = min(numbers)

print(f"A soma de todos os números é: {soma}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#achar segundo maior
#numbers.pop(numbers.index(max(numbers)))
#print(f"O segundo maior número é: {max(numbers)}")

numbers = sorted(numbers)
print(numbers)
print(f"O segundo maior número é: {numbers[-2]}")
