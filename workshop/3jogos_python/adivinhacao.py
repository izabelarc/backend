from random import randint 
random_number = randint(1,100)

print(random_number)

numero = input("Digite um número: ")

while numero != random_number:
    if numero.isdigit():
        while numero != random_number:
            try:
                numero = int(input("Errou. Digite outro número: "))
            except:
                print("Você não digitou um número.")
    else:
         numero = input("Você não digitou um número. Digite um número: ")
    
print("Você acertou!")