from random import randint 

series = ["Wednesday", "The Walking Dead", "Anne with an E", "Blind Spot", "Round 6"]

rates = []

'''for serie in series:
    print(serie) #percorrer a lista toda'''
for count in range (0,6):
    rate = int(input(f"Quantas estrelas para {series[count]}"))
    rates.append(rate)
    
print(series)
print(rates)