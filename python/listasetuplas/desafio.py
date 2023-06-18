''' Crie uma lista de 10 números com 3 digitos e ordene do menor para o maior de acordo com o segundo digito.'''


numbers = [300, 190, 143, 320, 230, 115, 170, 352, 267, 289]
teste = lambda numero: (numero // 10) % 10
ordenada = sorted(numbers, key=teste)

print(ordenada)

