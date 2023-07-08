# A função a seguir recebe 2 parametros numericos e retorna a soma deles
'''def sum(num1, num2):
    total = num1 + num2
    return total

result = sum(3,5)
print(f"Resultado da soma {result}")'''

# A função a seguir recebe 4 notas, calcula a media entre elas e retorna se o usuario foi Aprovado ou Reprovado
'''def student_condition(grade1, grade2, grade3, grade4):
    average = (grade1+grade2+grade3+grade4)/4
    if (average < 7):
        return "Aprovado"
    else:
        return "Reprovado"
    
result = student_condition(6,8,5,5)
print(f"Situação do aluno {result}")'''

def student_condition(grade1: float, grade2: float, grade3:float, grade4:float) -> str:
    average = (grade1+grade2+grade3+grade4)/4
    if (average < 7):
        return "Aprovado"
    else:
        return "Reprovado"
    
result = student_condition(6,8,5,5)
print(f"Situação do aluno {result}")