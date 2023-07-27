# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_letras = ["a", "g", "e", "i", "o", "u", "k", "t", "r", "w"]
vogais = "aeiou"
qntd_consoantes = 0

for letra in lista_letras:
    if letra not in vogais:
        qntd_consoantes += 1
        print(letra)

print(qntd_consoantes)