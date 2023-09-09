class Aluno:
    def __init__(self, nome: str, idade:int) -> None:
        self.nome = nome
        self.idade = idade
        
    def nome_aluno(self) -> str:
        return self.nome
    
    def idade_aluno(self) -> int:
        return self.idade