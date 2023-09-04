# Considere o seguinte dicionário em Python:
# pessoas = {
#     "João": 23,
#     "Maria": 28,
#     "Pedro": 35,
#     "Lucas": 19
# }

# a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.

# b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.

# c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.

pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}
idade_joao=pessoas["João"] 
print(f"A idade de João é: {idade_joao}")

pessoas["Ana"]=31
print(pessoas)

def maior_idade(dicionario):
    maior = max(dicionario.values())
    for nome, idade in dicionario.items():
        if idade == maior:
            return nome
pessoa_mais_velha = maior_idade(pessoas)
print(f"A pessoa mais velha é {pessoa_mais_velha}.")