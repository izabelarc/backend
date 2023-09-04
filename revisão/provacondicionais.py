email_cadastrado = "infinity@email.com"
senha_cadastrada = "senha123"

while True:
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login bem-sucedido! Você está conectado.")
        break  
    else:
        print("Credenciais incorretas. Tente novamente.")





