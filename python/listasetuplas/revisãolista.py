from random import randint 

series = ['Wednesday', 'The Walking Dead', 'Anne with an E', 'Blind Spot', 'Round 6']
'''for serie in series:
    print(serie) #percorrer a lista toda'''

rates = []
random_num_list = []
count = 0

while count < 5:
    random_num = randint(0,4)
    if random_num not in random_num_list:
        rate = int(input(f'Quantas estrelas para a serie {series[random_num]} '))
        count += 1
        rates.append((series[random_num], rate))
        random_num_list.append(random_num)
    
for rate in rates:
    series_name = rate[0]
    series_rate = rate[1]
    print(f"Serie {series_name} - {series_rate}")
    
'''from random import randint 

series = ['Wednesday', 'The Walking Dead', 'Anne with an E', 'Blind Spot', 'Round 6']

#ERRADO rates = [] ERRADO#
rates = [0,0,0,0,0]
random_num_list = []
count = 0

while count < 5:
    random_num = randint(0,4)
    if random_num not in random_num_list:
        rate = int(input(f'Quantas estrelas para a serie {series[random_num]} '))
        count += 1
        rates[random_num] = rate
        #ERRADO rates.insert(random_num, rate) ERRADO#
        random_num_list.append(random_num)
    
for index in range(5):
    print(f"Serie {series[index]} - {rates[index]}")'''