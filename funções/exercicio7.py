'''Crie uma função em python que verifica se o usuário digitou um e-mail válido:
deve possuir pelo menos um caracter @ e um caracter . após o @'''

def email_valido(email):
    posicao_ponto = email.find(".")
    posicao_arroba = email.find("@")
    if "@" in email:
        if posicao_ponto > posicao_arroba:
            return print("Esse formato é de e-mail é válido")
        else:
            return print("Esse formato de e-mail é inválido")
    else:
        return print("Esse formato de e-mail é inválido")
        
variavel = input("Digite seu e-mail: ")

email_valido(variavel)
