
# def calcular(entrada):
#     operadores = "+-*/"
#     partes = entrada.split() #separa string
    
#     if len(partes) != 3:
#         return "Formato inválido. Use: número operador número"
    
#     num1, operador, num2 = partes
    
#     if operador not in operadores:
#         return "Operador inválido. Use +, -, *, ou /"
    
#     for char in num1 + num2:
#         if char not in "0123456789":
#             return "Número inválido. Use apenas dígitos de 0 a 9."
    
#     if operador == "+":
#         resultado = (int(num1) + int(num2))
#     elif operador == "-":
#         resultado = (int(num1) - int(num2))
#     elif operador == "*":
#         resultado = (int(num1) * int(num2))
#     elif operador == "/":
#         if num2 != "0":
#             resultado = (int(num1) / int(num2))
#         else:
#             return "Divisão por zero não é permitida"
    
#     return resultado

def encontrar_numeros_operador(entrada):
    operadores = "+-*/"
    num1 = ""
    operador = ""
    num2 = ""
    num1_encontrado = False

    for char in entrada:
        if char in operadores:
            if num1_encontrado:
                operador = char
            else:
                num1_encontrado = True
        elif num1_encontrado:
            num2 += char
        else:
            num1 += char

    return num1, operador, num2

def calcular(entrada):
    num1, operador, num2 = encontrar_numeros_operador(entrada)

    if not num1 or not operador or not num2:
        return "Formato inválido. Use: número operador número"

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Número inválido. Use apenas números."

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Divisão por zero não é permitida"
    else:
        return "Operador inválido. Use +, -, *, ou /"

    return resultado