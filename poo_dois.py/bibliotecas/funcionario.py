from bibliotecas.pessoa import *

class Funcionario(Pessoa):
    def __init__(self, nome:str, idade:int, sexo:str, matricula:int) -> None:
        super().__init__(nome, idade, sexo)
        self.matricula =matricula
        
    def cracha(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
    
    def identidade(self) -> None:
        return super().idenitidade()
    
    def envelhecer(self) -> None:
        return super().envelhecer()