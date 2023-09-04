
produtos = []
total_produtos = 0


def adicionar_produto():
    global total_produtos
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    total = quantidade * valor_unitario
    produto = {"produto": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total}
    produtos.append(produto)
    total_produtos += total
    print(f"{nome} foi adicionado à lista de compras.")


def ver_lista():
    print("\nLista de Compras:")
    for produto in produtos:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
    print(f"Total da lista: R${total_produtos:.2f}")


def atualizar_produto():
    global total_produtos
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in produtos:
        if produto['produto'] == nome:
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
            quantidade = int(input("Digite a nova quantidade: "))
            valor_unitario = float(input("Digite o novo valor unitário: "))
            produto['quantidade'] = quantidade
            produto['valor'] = valor_unitario
            produto['total'] = quantidade * valor_unitario
            total_produtos -= produto['total']
            total_produtos += quantidade * valor_unitario
            print(f"{nome} foi atualizado na lista de compras.")
            return
    print(f"Produto {nome} não encontrado na lista de compras.")


def remover_produto():
    global total_produtos
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in produtos:
        if produto['produto'] == nome:
            total_produtos -= produto['total']
            produtos.remove(produto)
            print(f"{nome} foi removido da lista de compras.")
            return
    print(f"Produto {nome} não encontrado na lista de compras.")


while True:
    print("\nOpções:")
    print("1. Adicionar produtos")
    print("2. Ver a lista de produtos")
    print("3. Atualizar produtos")
    print("4. Remover produto")
    print("5. Encerrar programa")
    
    opcao = input("Escolha uma opção (1/2/3/4/5): ")
    
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        ver_lista()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")