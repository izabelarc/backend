'''Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência 
até que ele acerte. Para ajudar o usuário, o programa deve informar se o número é maior ou menor que 
o número a ser adivinhado. Ao final, imprima o número adivinhado e a quantidade de tentativas.'''

from random import randint
random_number = randint(1,100)

print(random_number)

numero = int(input("Digite um número para tentar adivinhar: "))
tentativas = 0

while numero != random_number:
    tentativas+=1
    if numero > random_number:
        numero = int(input("O número que você digitou é maior. Digite outro número: "))
    elif numero < random_number:
        numero = int(input("O número que você digitou é menor. Digite outro número: "))

tentativas += 1
print("Parabéns, você acertou o número: ", random_number)
print("O número de tentativas foi: ", tentativas)

