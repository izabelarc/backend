# Exercícios - Lógica de programação em Python

# Fundamentos:

# 1  - Crie um algoritmo que exiba na tela (terminal) a mensagem "Olá Mundo".
print("Olá Mundo")

# 2  - Crie um algoritmo que exiba na tela (terminal) seu nome. Por exemplo: "Olá, João Paulo."
nome = input("Insira seu nome: ")
print("Olá, ", nome)

# 3  - Crie um algoritmo que exiba na tela (terminal) sua idade. Por exemplo: 17.
idade = int(input("Insira sua idade: "))
print(idade)

# 4  - Crie um algoritmo que exiba na tela (terminal) (em linhas separadas) seu nome e sua idade.
print("Seu nome:",nome,"\n","Sua idade: ",idade)

# 5  - Crie um algoritmo que exiba na tela (terminal) (na mesma linha) seu nome e sua idade.
print("Nome: ",nome,"idade:",idade)

# 6  - Crie um algoritmo que exiba na tela (terminal) a soma de dois números inteiros.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
print("A soma é: ", soma)

# 7  - Crie um algoritmo que exiba na tela (terminal) a subtração de dois números inteiros.
subtração = numero1 - numero2
print("A subtração é: ", subtração)

# 8  - Crie um algoritmo que exiba na tela (terminal) a multiplicação de dois números inteiros.
multiplicação = numero1 * numero2
print("A multiplicação é: ", multiplicação)

# 9  - Crie um algoritmo que exiba na tela (terminal) a divisão de dois números inteiros.
divisão = numero1 / numero2
print("A divisão é: ", divisão)

# 10 - Crie um algoritmo que exiba na tela (terminal) o resto da divisão de dois números inteiros.
resto = numero1 % numero2
print("O resto é: ", resto)

# 11 - Crie um algoritmo que exiba na tela (terminal) apenas a parte inteira de uma divisão de dois números inteiros.
divisão_int = numero1 // numero2
print("A parte inteira da divisão é: ", divisão_int)

# 12 - Crie um algoritmo que exiba na tela (terminal) o quadrado de um número inteiro.
quadrado = numero1 ** numero2
print("O quadrado é: ", quadrado)

# 13 - Crie um algoritmo que exiba na tela (terminal) o valor lógico de uma variável qualquer.
variavel = True
print("O valor lógico é: ", variavel)

# 14 - Crie um algoritmo que exiba na tela (terminal) o tipo de uma variável cujo valor atribuído é "jpaulo@infinityschoool.com.br".
variavel1 = "jpaulo@infinityschool.com.br"
print("O tipo é: ", type(variavel1))

# 15 - Crie um algoritmo que exiba na tela (terminal) o tipo de uma variável cujo valor atribuído é "c".
variavel2 = "c"
print("O tipo é: ", type(variavel2))

# 16 - Crie um algoritmo que exiba na tela (terminal) o tipo de uma variável cujo valor atribuído é 12.
variavel3 = 12
print("O tipo é: ", type(variavel3))

# 17 - Crie um algoritmo que exiba na tela (terminal) o tipo de uma variável cujo valor atribuído é 1.87.
variavel4 = 1.87
print("O tipo é: ", type(variavel4))

# 18 - Crie um algoritmo que exiba na tela (terminal) o tipo de uma variável cujo valor atribuído é False.
variavel5 = False
print("O tipo é: ", type(variavel5))

# 19 - Crie um algoritmo que concatene duas strings ao ser executado. Exiba a string concatenada na tela (terminal).
string1 = "Olá,"
string2 = "mundo!"

concatenada = "".join([string1, string2])
print("A concatenação é: ", concatenada)

# 20 - Crie um algoritmo que concatene dois numeros inteiros ao ser executado. Exiba os números concatenados na tela (terminal).
concatenada1 = numero1, numero2
print("A concatenação é: ", concatenada1)
