''' Crie um programa que leia dois valores e mostre um menu para calcular: 1- somar, 2- subtrair, 3- multiplicar, 4- dividir e 5- sair'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

opt = 0

while opt != 5:
    print ("----------")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    print("[5] - Sair")
    print("----------")
    
    opt = int(input(">Digite uma opção< "))
    
    if opt == 1:
        resultado = num1 + num2
        print("O resultado da soma é: ", resultado)
    elif opt == 2:
        resultado = num1 - num2
        print("O resultado da subtração é: ", resultado)
    elif opt == 3:
        resultado = num1 * num2
        print("O resultado da multiplicação é: ", resultado)
    elif opt == 4:
        resultado = num1 / num2
        print("O resultado da divisão é: ", resultado)
    elif opt == 5:
        print ("O programa está sendo finalizado...")
        
print("Fim do programa.")