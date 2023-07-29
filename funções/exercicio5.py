''' Crie uma função em Python que calcule o fatorial de um número digitado pelo usuário. 
Dica: Fatorial é a multiplicação de todos os números menores que ele e ele.'''
'''def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input("Digite um número: "))
result = fatorial(numero)

print(f"O fatorial é: {result}")'''

def fatorial(n):
    
    if numero == 0 or numero ==1:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado

numero = int(input("Digite um número: "))
resultado = fatorial(numero)

print(f"O fatorial é: {resultado}")
