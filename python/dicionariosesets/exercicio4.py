'''Refaça o programa anterior (exercicio3) e imprima a lista dos alunos aprovados em ordem decrescente (da maior
média para a menor)'''

data = {}
notas = []
aprovados = []
anterior = 0

for y in range(4):
    name = input("Digite seu nome: ")
    data["nome"] = name
    soma = 0
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
            
    media = 0
    media = soma/4
    data["media"] = media

    if media >= 7:
        situation = "Aprovado"
        dic_aprovados = {"nome": name, "media": media}
        if media >= anterior:
            aprovados.append(dic_aprovados)
        else: 
            aprovados.insert(-1, dic_aprovados)
        anterior = media
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
    
print(aprovados)