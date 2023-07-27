# Faça uma função para calcular o valor/hora de um funcionário.

def div(valor: float, hora: float) -> str:
    total = valor/hora
    return total

valor = float(input("Digite seu salário: "))
hora = float(input("Digite quantas horas trabalha por dia: "))

result = div(valor, hora)
print(f" O valor for hora é: {result}")