
alunos = {}

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno com matrícula {matricula} adicionado com sucesso!")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno com matrícula {matricula} removido com sucesso!")
    else:
        print("Matrícula não encontrada. Nenhum aluno removido.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = nome
        print(f"Nome do aluno com matrícula {matricula} atualizado com sucesso!")
    else:
        print("Matrícula não encontrada. Nenhum aluno atualizado.")

def VerAlunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
