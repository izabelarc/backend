series = ["Breaking Bad", "Game of Thrones", "The Walking Dead", "Wednesday", "Friends", 
          "Stranger Things", "Black Mirror", "La casa de Papel", "Prison Break", 
          "Rings of Power", "You", "Pânico"]

print('_' * 15)
print("Minha lista de Séries")
print('_' * 15)
print(f"As 5 primeiras são: {series[0:5]}")
print("As últimas 4 séries são: ", series[-4:])
print(f"Séries em ordem alfabética {sorted(series)}")
print(f"Stranger Things está na posição {series.index('Stranger Things')}")