# O sistema deve pedir para cadastro do time: O nome do time, a cidade onde o time
# fará os jogos como mandante e o nome do mascote do time.

class Time:
    def __init__(self) -> None:
        self.nome_time = None
        self.mandante = None
        self.mascote = None
        
    def entrada_time(self) -> None:
        self.nome_time = input("Digite o nome do time: ")
        self.mandante = input("Digite a cidade que será mandante: ")
        self.mascote = input("Digite o nome do mascote: ")
        
    def saida_time(self) -> None:
        print(f"O nome do time é: {self.nome_time}")
        print(f"A cidade em que será mandante é: {self.mandante}")
        print(f"O nome do mascote é {self.mascote}")