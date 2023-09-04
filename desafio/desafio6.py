'''Crie um programa de cadastro e confirmação de senha para 5 usuários. O programa deve solicitar e-mail, senha e confirmação de senha de cada um
OBS: o programa só solicita os dados do próximo usuário se a confirmação de senha estiver correta'''

for i in range (5):
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    confirma = input("Confirme sua senha: ")
    while confirma != senha:
        confirma = input("As senhas não batem, tente novamente: ")
    
    print("Cadastro realizado com sucesso.")