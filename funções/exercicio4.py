def sum(num1: int, num2: int) -> int:
    '''Calcula a soma de dois números'''
    soma = num1 + num2
    return soma

def sub(num1: int, num2: int) -> int:
    '''Calcula a subtração de 2 números'''
    subtraction = num1 - num2
    return subtraction

def mult(num1: int, num2: int) -> int:
    '''Calcula a multiplicação de 2 números'''
    multiplication = num1 * num2
    return multiplication

def div(num1: int, num2: int) -> float:
    '''Calcula a divisão de 2 números'''
    division = num1 / num2
    return division

numero1 = int(input("Digite um número: ")) # Insere primeiro número
numero2 = int(input("Digite outro número: ")) # Insere segundo número

'''Trás as opções'''
print("Essas são as suas opções: ")
print("+: Soma")
print("-: Subtração")
print("*: Multiplicação")
print("/: Divisão")
'''Escolhe a opção'''
opcao = input("Digite o símbolo opção que você deseja:")

'''Condicional para a opção escolhida'''
if(opcao=="+"):
    result = sum(numero1, numero2)
    print(f"O valor da soma é: {result}")
elif(opcao=="-"):
    result = sub(numero1, numero2)
    print(f"O valor da subtração é: {result}")
elif(opcao=="*"):
    result = mult(numero1, numero2)
    print(f"O valor da multiplicação é: {result}")
elif(opcao=="/"):
    if (numero2==0):
        '''Trás o erro de divisão por 0'''
        print("Não é possível dividir por 0")
    else:
        result = div(numero1, numero2)
        print(f"O valor da divisão é: {result}")