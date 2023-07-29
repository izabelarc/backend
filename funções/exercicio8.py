'''Crie uma função que verifica se uma senha é forte ou fraca, sendo:
até 5 caracteres > fraca
letras e números > forte
letras, numeros e pontuação > muito forte'''

import string

def caracteres_senha(sen):
        letras = any(a.isalpha() for a in sen)
        numero = any(a.isdigit() for a in sen)
        pontuacao = any(a in string.punctuation for a in sen)
        
        if letras and numero and pontuacao:
            return "Sua senha é muito forte"
        elif letras and numero:
            return "Sua senha é forte"
        elif letras:
            return "Sua senha é fraca"
        else:
            return "Sua senha deve conter letras e números."
        
def nivel_senha(s):
    if len(s) < 5:
        print("Sua senha é fraca")
    else:
        mensagem = caracteres_senha(s)
        print(mensagem)
        
senha = input("Digite sua senha: ")

nivel_senha(senha)