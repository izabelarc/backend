#2. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.
i = 0
soma = 0
resultado = 0

while i < 3:
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    soma += altura
    i += 1
    media = soma / i
if idade > 13 and altura < media:
    resultado += 1
print(resultado)

