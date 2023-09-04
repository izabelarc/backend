from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(lambda x: x ** 2, numeros))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

soma_total = reduce(lambda x, y: x + y, numeros)

print("Quadrados dos números:", quadrados)
print("Números pares:", numeros_pares)
print("Soma de todos os números:", soma_total)
