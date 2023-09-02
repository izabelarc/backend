class Pessoa:
    def __init__(self, nome: str, idade:int, sexo:str) -> None:
        '''
        Método inicializador
        '''
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
    def identidade (self) -> None:
        print("CARTEIRA DE IDENTIDADE")
        print(f"NOME: {self.nome}")
        print(f"IDADE: {self.idade}")
        print(f"SEXO: {self.sexo}")
        
    def envelhecer(self) -> None:
        self.idade += 1
    
    def saudacao(self, saudacao: str) -> None:
        print(f"{saudacao}, {self.nome}")