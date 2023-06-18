'''Crie um programa em python que escolhe um número aleatório entre 0 e 5. Em seguida, peça ao usuário para tentar descobrir qual foi o número escolhido.
O programa deve solicitar ao usuário para digitar um número quantas vezes for necessário até que ele acerte. Ao acertar, o programa deve parar e mostrar quantos palpites foram necessários.'''

'''from random import randint #random é um arquivo que tem função randint que pega números inteiros aleatórios, tem que importar

random_number = randint(0,5)

print(random_number)

numero=int(input("Digite um número entre 0 e 5 para tentar adivinhar: "))
palpites = 1

while numero != random_number:
    numero = int(input("Você errou. Digite outro número: "))
    palpites += 1
    
print("Você acertou. O número de tentativas foi: ", palpites)'''

'''Aumentar o random para 0 a 20 e a cada solicitação, informar ao usuário se o número que ele digitou é maior ou menor'''

from random import randint 
random_number = randint(0,20)

print(random_number)

numero=int(input("Digite um número entre 0 e 20 para tentar adivinhar: "))
palpites = 1

while numero != random_number:
        if (numero > random_number):
            numero = int(input("O número que você digitou é maior. Digite outro número: "))
        elif (numero < random_number):
            numero = int(input("O número que você digitou é menor. Digite outro número: "))   
        palpites += 1
    
print("Você acertou. O número de tentativas foi: ", palpites)