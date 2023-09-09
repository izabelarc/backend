from pacotes.aluno import Aluno

class BancoDeDados:
    def __init__(self, dados:list) -> None:
        self.dados = dados
        
    def mostrar_dados(self) -> None:
        for dado in self.dados:
            print(f"ID: {self.dados.index(dado)+1}")
            print(f"Nome: {dado.nome_aluno()}")
            print(f"Idade: {dado.idade_aluno()}\n")
            
    def mostrar_dados2(self) -> None:
        indice = 1
        for dado in self.dados:
            print(f"ID: {indice}")
            print(f"Nome: {dado.nome_aluno()}")
            print(f"Idade: {dado.idade_aluno()}\n")
            indice += 1
    
    def mostrar_dados3(self) -> None:
        for indice, dado in enumerate(self.dados):
            print(f"ID: {indice+1}")
            print(f"Nome: {dado.nome_aluno()}")
            print(f"Idade: {dado.idade_aluno()}\n")
            
    def mostrar_dado(self, id:int) -> None:
        print(f"ID: {id}")
        print(f"Nome: {self.dados[id-1].nome_aluno()}")
        print(f"Idade: {self.dados[id-1].idade_aluno()}")
        
    def adicionar_dado1(self, nome:str, idade:str) -> None:
        self.dados.append(Aluno(nome,idade))
        self.mostrar_dado(len(self.dados))
        
    def adicionar_dado2(self, aluno: Aluno) -> None:
        self.dados.append(aluno)
        self.mostrar_dado(len(self.dados))
        
