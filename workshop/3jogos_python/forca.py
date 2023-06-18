# Desafio 3

# Criar um jogo da Forca.
# Utilizando a lista de frutas, criaremos um jogo da Forca.
# O Computador deve escolher uma palavra secreta da lista.
# O jogador deve tentar adivnhar letra por letra.
# O número máximo de tentativas é 6. 
# A palavra deve ser exibida parcialmente na medida em que o jogador vai acertando.
# Ex: se a palavra secreta for morango e tentaram a letra 'o':
# deve ser exibido:  _ o _ _ _ _ o
# O jogador não deve perder tentativas ao tentar repetir uma letra, mas deve ser avisado
# que já tentou aquela letra.
# O número de tentativas deve ser exibido a cada vez que o jogador falha!!!
# Quando chegar a 0 tentativas o jogador mor... perde...
# Caso consiga advinhar a palavra, uma mensagem deve ser exibida para comemorar
# a gloriosa e improvável vitória de nosso jogador.

import random 

fruits = ["Abacate", "Abacaxi", "Açaí", "Acerola", "Ameixa", "Amora", "Ananás", "Arando", "Banana", "Cacau", "Caqui", "Carambola", "Cereja", "Coco", "Cranberry", "Cupuaçu",
    "Damasco", "Dióspiro", "Damasqueiro", "Figo", "Framboesa", "Fruta-do-conde", "Goiaba", "Groselha", "Jabuticaba", "Jaca", "Jambo", "Jamelão", "Jenipapo", "Kiwi", "Laranja", "Limão",
    "Maçã", "Mamão", "Manga", "Maracujá", "Melancia", "Melão", "Mirtilo", "Morango", "Nectarina", "Noz", "Pera", "Pêssego", "Pitanga", "Romã", "Tangerina", "Uva",
    "Acerola", "Amêndoa", "Ameixa", "Atemoia", "Bacaba", "Bacuri", "Bergamota", "Buriti","Cacau", "Cagaita", "Caju", "Caqui", "Cereja", "Cereja-do-rio-grande", "Cítricos", "Coco",
    "Cupuaçu", "Cupuassu-do-amazonas", "Figo", "Framboesa", "Fruta-de-conde", "Fruta-do-lobo", "Fruta-pão", "Goiaba","Goiaba-de-anta", "Graviola", "Groselha", "Ingá", "Jabuticaba", 
    "Jaca", "Jamelão", "Jenipapo", "Juá", "Jujuba", "Kiwi", "Laranja", "Lichia", "Limão", "Maçã", "Mamão", "Manga", "Maracujá", "Melancia", "Melão", "Morango", "Nectarina", 
    "Pera", "Pêssego","Pitanga", "Romã", "Tangerina", "Uva"]

def jogo_da_forca():
    palavra = random.choice(fruits)
    palavra_secreta = ['_'] * len(palavra)
    tentativas = 6
    letras_erradas = []

    while tentativas > 0:
        print('Adivinhe a palavra: ', ' '.join(palavra_secreta))
        print('Letras erradas: ', ' '.join(letras_erradas))
        print('Tentativas restantes: ', tentativas)

        letra = input('Digite uma letra: ')

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        if tentativas == 0:
            print('Você perdeu! A palavra era', palavra)
            break

        if '_' not in palavra_secreta:
            print('Parabéns! Você ganhou! A palavra era', palavra)
            break

jogo_da_forca()
