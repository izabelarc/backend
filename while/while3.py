
name = input ("Digite seu nome: ")
salary = 0
gender = ""

while gender != "M" and gender != "F" and gender != "m" and gender != "f":
    gender = input("Digite seu gênero: ")

while salary < 1500:
    salary = float(input("Digite seu salário: "))
    
print("Agora sim, fim do programa")

"""
name = input ("Digite seu nome: ")
salary = float(input("Digite seu salário: "))
gender = input("Digite o sexo: ")
while gender != "m" and gender != "f" and gender != "M" and gender != "F":
    gender = input("Sexo inválido. Digite novamente: ")
    
while salary < 1500:
    salary = float(input("Salário tem que ser maior que 1500. Digite novamente: "))
"""