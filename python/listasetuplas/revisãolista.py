from random import randint 

series = ["Wednesday", "The Walking Dead", "Anne with an E", "Blind Spot", "Round 6"]

rates = []
random_num_list = []

'''for serie in series:
    print(serie) #percorrer a lista toda'''

for count in range (0,6):
    random_num = randint(0,5)
    if random_num not in random_num_list:
        rate = int(input(f"Quantas estrelas para {series[random_num]}?"))
    rates.append(rate)
    random_num_list.append(random_num)
    
print(series)
print(rates)