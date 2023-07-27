dados = {"nome": "Luan", "idade": 35, "email": "luan@gmail.com"}

dados_lista = ["Luan", 35, "luan@gmail.com"]

#pegar idade do dicionario dados
valor_idade = dados["idade"]
print(valor_idade)

#alterando valor de uma chave específica
dados["email"] = "luanferreira@yahoo.com"

#adcionar uma chave ao dicionário
dados["empresa"] = "Infinity School"
print(dados)

#list retorna as chaves daquele dicionario
print(list(dados))

#items retorna uma lista com uma tupla separados chave valor | importante para o for
print(dados.items())

for chave, valor in dados.items():
    print(chave, "-", valor)
    
#podemos ter uma chave que contém uma lista
dados2 = {
    "nome": "Diana",
    "idade": 30,
    "email": "diana@gmail.com",
    "linguagens": ["Python", "Java", "PHP"]
}

# Criar um programa que solicita ao usuario seus dados nome, sexo, estado civil e naturalidade e armazene estes dados num dicionario
user_name = input("Digite seu nome: ")
user_gender = input("Digite seu sexo: ")
user_status = input("Digite seu estado civil: ")
user_from = input("Digite o nome da cidade que nasceu: ")

user_data = {
    "name": user_name,
    "gender": user_gender,
    "status": user_status,
    "from": user_from 
}

for key, value in user_data.items():
    print(f"{key}: {value}")

#update atualiza o valor da chave
dados2.update({"status": "casado"})

