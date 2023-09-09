def calcular(entrada):
    operadores = "+-*/"
    partes = entrada.split() #separa string
    
    if len(partes) != 3:
        return "Formato inválido. Use: número operador número"
    
    num1, operador, num2 = partes
    
    if operador not in operadores:
        return "Operador inválido. Use +, -, *, ou /"
    
    for char in num1 + num2:
        if char not in "0123456789":
            return "Número inválido. Use apenas dígitos de 0 a 9."
    
    if operador == "+":
        resultado = str(int(num1) + int(num2))
    elif operador == "-":
        resultado = str(int(num1) - int(num2))
    elif operador == "*":
        resultado = str(int(num1) * int(num2))
    elif operador == "/":
        if num2 != "0":
            resultado = str(int(num1) / int(num2))
        else:
            return "Divisão por zero não é permitida"
    
    return resultado
