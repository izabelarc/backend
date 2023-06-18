sum_of_salary = 0
count_of_people = 0

for count in range(0,5):
    salary = float(input("Digite o salário: "))
    num_of_children = int(input("Número de filhos: "))
        
    if salary <= 1500:
        count_of_people += 1 #count_of_people = count_of_people + 1

    if num_of_children > 3:
        sum_of_salary += salary #sum_of_salary = sum_of_salary + salary
    
print("Recebem até 1.500,00", count_of_people)
print("Soma dos salários de quem tem mais de 3 filhos: ", sum_of_salary)