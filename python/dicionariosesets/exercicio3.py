#Refaça o programa anterior (exercicio2), mas desta vez, para 7 alunos e imprima na tela todos os dados dos alunos

data = {}
notas = []
soma = 0

for i in range(7):
    name = input("Digite seu nome: ")
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
        
    notas.clear()
    