
''' indice SEMPRE contado a partir do 0 
len(nomedalista) qntd de itens na lista
nomelista.append(nomeitem) adiciona novo item ao final da lista
nomedalista.insert(2, nomeitem) adiciona novo item em um local específico
nomedalista.pop() exclui o ultimo item
nomedalista.pop(2) remove o item com numero de índice indicado
nomedalista.remove(nomeitem) remove o item pelo nome dele [SE O ITEM SE REPETIR NA LISTA, REMOVE SOMENTE O PRIMEIRO]
nomedalista.count(nomeitem) conta quantos itens daquele tem na lista
nomedalista[-4:0] trás os ultimos 4 itens da lista
sorted(nomedalista) vai deixar em ordem alfabetica
nomedalista.index(nomedoitem) vai trazer a posição do item na lista e se colocar +1 trás a posição real da lista
nomedalista.clear() exclui todos os itens da lista
nomedalista.copy() retorna copia da lista
x = nomedalista.count(nomedoitem) trás quantas vezes o item se repete na lista
nomedalista.extend(nomelista2) adiciona uma lista a outra
nomedalista.revert() inverte a lista toda'''

'''#criando listas: 
names = []

numbers = [10, 5, 7, 9, 1]'''

products = ["notebook","headset", "mouse", "teclado", "headset"] #string entre aspas

#imprimindo um produto:
print(products[2])

#trazendo quantidade de itens da lista:
print("Ao todo temos: ", len(products), "produtos.")

#trazendo os items da lista:
for product in products: 
    print(product)

#inserindo item ao final da lista:    
products.append("monitor")

#inserir item na posição x da lista:
products.insert(2, "gabinete")

#excluindo o ultimo item da lista:
products.pop()

#excluindo o item da posição x da lista:
products.pop(1)

#excluindo pelo nome do item da lista:
products.remove("headset")
    
#contando quantos itens x tem na lista:
products.count("mouse")

