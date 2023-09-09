class Database:
    def __init__(self, lista: list) -> None:
        self.lista = lista
        
    def mostrar_cadastros(self) -> None:
        for aluno in self.lista:
            print(f"ID: {self.lista.index(aluno)+1}")
            print(f"Nome: {aluno.get('nome')}")
            print(f"Idade: {aluno.get('idade')}\n")
            
    def mostrar_cadastro(self, id: int) -> None:
        print(f"ID: {id}")
        print(f"Nome: {self.lista[id-1].get('nome')}")
        print(f"Nome: {self.lista[id-1].get('idade')}")
        
    def cadastrar_aluno(self, nome:str, idade:int) -> None:
        self.lista.append({"nome": nome, "idade": idade})
        print("Aluno(a) cadastrado(a) com sucesso! \n")
        
        self.mostrar_cadastro(len(self.lista))
