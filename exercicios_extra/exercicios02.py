# Exercícios - Lógica de programação em Python

# Input - para os exercícios abaixo você precisará utilizar o método input(), 
#para requisitar dados externos ao programa:

# 26 - Crie um algoritmo que ao ser executado receba um nome do usuário (através de um input), armazene essa informação numa variável
# e imprima o valor do tipo dessa variável no terminal.
nome = input("Digite seu nome completo: ")
tipo = type(nome)
print("O tipo da variável é: ", tipo)

#27 - Crie um algoritmo que ao ser executado receba um número (através de um input) e armazene essa informação numa variável.
# - Qual é o tipo de variável que será retornado? (Só pense)
# - Imprima o valor do tipo dessa variável no terminal.
# - Compare sua resposta com o resultado, foi o mesmo? 
# Foi diferente? E se foi diferente, por que você acha que foi diferente?
numero = input("Digite um número: ")
tipo_numero = type(numero)
print ("O tipo da variavel numero é:", tipo_numero)
'''      o tipo varia de acordo com a variável declarada antes do input, 
         se não colocar nada str se colocar sera float ou int'''


# 28 - Desafio: Crie um algoritmo que recebe dois valores númericos e qual operação 
# o usuário deseja realizar e realize essa operação. Por exemplo:
# O usuário forneceu as seguintes entradas: 4, 5, multiplicação.
# Ele deseja multiplicar 4 e 5 e ser informado do resultado.
# Mas numa próxima execução do programa talvez ele queira utilizar outros valores
# ou fazer outra operação... e aí, como fazer? 


# 29 - Desafio: Considere o desafio 28, imagine que o teclado de um usuário sempre 
# coloca um espaço quando ele digita um número. Ex: Se ele digita 4, que o chega para nós é: "4 "
# Isso fará com que, mesmo que ele tenha digitado um número, ele não consiga realizar a operação.
# Como prevenir/corrigir esse erro?


# 30 - Desafio: Crie um algoritmo que rece
# o nome, idade, a fruta favorita e se o usuário é ou não aluno da Infinity School.
# Imprima os valores no seguindo o exemplo:
# Se as informações forem: "João", 34, "banana", as informações devem aparecer dessa forma no terminal:
# Nome: João
# Idade: 34
# Fruta favorita: banana
# Aluno Infinty: Sim  