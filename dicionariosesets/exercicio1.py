# Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos.

user_name = input("Digite seu nome: ")
user_surname = input("Digite seu sobrenome: ")
user_age = int(input("Digite sua idade: "))
user_email = input("Digite seu email: ")
i = 0
user_data = {
    "name": user_name,
    "surname": user_surname,
    "age": user_age,
    "email": user_email
}

for key, value in user_data.items():
    i += 1
    print(f"{i}. {key} - {value}")