par = lambda string : True if string[-1] in "02468" else False

numero = input("Digite um número: ")

#Primeiro exemplo
print(par("par"))

#Segundo exemplo
print(f"O número {numero} é par." if par(numero) else f"O número {numero} é ímpar.")