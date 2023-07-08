# Crie uma função para calcular o IMC de 4 pessoas.
# Atenção: Use as seguintes estruturas:
# -laço de repetição.
# -listas

vetor_imc = []

def calcular_imc(peso: float, altura: float):
    imc = peso / altura**2
    return imc

for i in range(4):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    result = calcular_imc(peso, altura)
    vetor_imc.append(result)
    i += 1

print(f"Os IMCs são: {vetor_imc}")
