# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima
# a idade e a altura na ordem inversa a ordem lida.
i = 0
vetor_idade = []
vetor_altura = []

while i<5:
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    vetor_idade.append(idade)
    vetor_altura.append(altura)
    i += 1

vetor_idade.reverse()
vetor_altura.reverse()

print(f"Ordem inversa da idade: {vetor_idade}")
print(f"Ordem inversa da altura: {vetor_altura}")

