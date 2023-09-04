
numeros_pares = []
numeros_impares = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

tupla_impares = tuple(numeros_impares)

print("Números pares:", numeros_pares)
print("Números ímpares:", tupla_impares)

quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)

soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
