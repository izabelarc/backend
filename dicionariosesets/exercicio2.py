'''Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
a. Nome do aluno
b. As 4 notas obtidas
c. Maior nota
d. Menor nota
e. Média
f. Situação
g. Aprovado se média for maior ou igual a 7
h. Reprovado se média for menor que 7
Agora imprima as informações deste aluno na saída padrão'''
data = {}
notas = []
name = input("Digite seu nome: ")
soma = 0

data["nome"] = name

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    i += 1
    soma += nota
    if i == 1:
        data["nota1"] = nota
    elif i == 2:
        data["nota2"] = nota
    elif i == 3:
        data["nota3"] = nota
    else:
         data["nota4"] = nota

media = soma/i
data["media"] = media

if media >= 7:
    situation = "Aprovado"
else:
    situation = "Reprovado"
data["situação"] = situation

maior = max(notas)
data["maior nota"] = maior

menor = min(notas)
data["menor nota"] = menor

for key, value in data.items():
    print(f"{key}: {value}")   