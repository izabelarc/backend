# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.

# O programa deve fornecer as seguintes funcionalidades:

# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

alunos = {}

while True:
    print("Opções:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1/2/3/4): ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        alunos[matricula] = nome
        print(f"Aluno {nome} com matrícula {matricula} adicionado com sucesso!")
    elif opcao == "2":
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in alunos:
            nome = alunos.pop(matricula)
            print(f"Aluno {nome} com matrícula {matricula} removido com sucesso!")
        else:
            print("Matrícula não encontrada. Nenhum aluno removido.")
    elif opcao == "3":
        if not alunos:
            print("Nenhum aluno registrado.")
        else:
            print("Lista de alunos e matrículas:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula}, Nome: {nome}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4).")
