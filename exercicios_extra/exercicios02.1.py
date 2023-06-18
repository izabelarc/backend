# Exercícios - Lógica de programação em Python

# Input - para os exercícios abaixo você precisará utilizar o método input() para requisitar dados externos ao programa:

# 1  - Crie um algoritmo em que o usuário informe uma frase qualquer e exiba a frase na tela (terminal) quando executado.
frase = input("Informe uma frase: ")
print(frase)

# 2  - Crie um algoritmo em que o usuário informe o nome completo e exiba o nome completo na tela (terminal) quando executado.
nome = input("Informe nome completo: ")
print(nome)

# 3  - Crie um algoritmo em que o usuário informe a idade e exiba a idade na tela (terminal) quando executado.
idade = int(input("Informe idade: "))
print(idade)

# 4  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba os números na tela (terminal) quando executado.
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
print(n1, n2)

# 5  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba a soma dos números na tela (terminal) quando executado.
soma = n1 + n2
print(soma)

# 6  - Crie um algoritmo em que o usuário informe dois números inteiros (x1 e x2) e exiba a diferença dos números na tela (terminal) quando executado.
x1 = int(input("Informe um número: "))
x2 = int(input("Informe outro número: "))
diferença = x1 - x2
print(diferença)

# 7  - Crie um algoritmo em que o usuário informe dois números inteiros (a1 e a2) e exiba o produto dos números na tela (terminal) quando executado.
a1 = int(input("Informe um número: "))
a2 = int(input("Informe outro número: "))
produto = a1 * a2
print(produto)

# 8  - Crie um algoritmo em que o usuário informe dois números inteiros (x e y) e exiba o quociente dos números na tela (terminal) quando executado.
x = int(input("Informe um número: "))
y = int(input("Informe outro número: "))
quociente = x / y
print(quociente)

# 9  - Crie um algoritmo em que o usuário informe quatro notas (n1, n2, n3 e n4). Após, calcule a média aritmética e exiba a média na tela (terminal) quando executado.
nota1 = int(input("Informe uma nota: "))
nota2 = int(input("Informe outra nota: "))
nota3 = int(input("Informe outra nota: "))
nota4 = int(input("Informe outra nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

# 10 - Crie um algoritmo em que o usuário informe quatro notas (n1, n2, n3 e n4) e seus respectivos pesos. Após, calcule a média ponderada e exiba a média na tela (terminal) quando executado.
not1 = int(input("Informe uma nota: "))
peso1 = int(input("Informe o peso: "))
not2 = int(input("Informe uma nota: "))
peso2 = int(input("Informe o peso: "))
not3 = int(input("Informe uma nota: "))
peso3 = int(input("Informe o peso: "))
not4 = int(input("Informe uma nota: "))
peso4 = int(input("Informe o peso: "))
ponderada = not1 * peso1 + not2 * peso2 + not3 * peso3 + not4 * peso4 / (peso1 + peso2 + peso3 + peso4)
print(ponderada)

# DESAFIO
# Crie um algoritmo em que o usuário informe dois números (n1 e n2) e qual o tipo de operação matemática que deseja realizar (adição, subtração,
# multiplicação ou divisão), por exemplo: n1 = 2; n2 = 6; operacao = '+'. Após, exiba na tela (terminal) o resultado da operação.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operador = input("Escolha o operador que deseja: +,-,*,/ ")

if operador == "+":
    print("{} + {} = {}".format(numero1, numero2, numero1+numero2))
elif operador == "-":
    print("{} - {} = {}".format(numero1, numero2, numero1-numero2))
elif operador == "*":
    print("{} * {} = {}".format(numero1, numero2, numero1*numero2))
else:
    print("{} / {} = {}".format(numero1, numero2, numero1/numero2))