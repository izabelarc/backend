# Faça uma função que retorne quantas letras possui uma palavra.
# Se for passado uma frase, a função deverá retornar o número de letras, espaços vazios e quantos
# sinais de pontuação.


import string
def qtd(palavra):
    total = len(palavra)
    return total

texto = input("Digite uma palavra: ")
result = qtd(texto)
print(f"A palavra tem {result} caracteres")

def contagem_frase(frase):
    letras = sum(c.isalpha() for c in frase)
    espacos = sum(c.isspace() for c in frase)
    pontuacao = sum(c in string.punctuation for c in frase)
    return letras, espacos, pontuacao

texto = input("Digite uma frase: ")
result = contagem_frase(texto)
print(f"O número de letras, espaços e pontuação respectivamente são: {result}")