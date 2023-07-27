# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.
contador_aluno = 0

for i in range(10):
    soma = 0
    for j in range(4):
        nota = float(input("Digite uma nota: "))
        soma += nota
    print(f"Media: {soma/4}")
    if (soma / 4) >= 7.0 :
        contador_aluno+=1

print(f"Número de alunos acima da média: {contador_aluno}")