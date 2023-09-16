# Para os jogadores, deverá ser possível cadastrar o nome do jogador, o nome do
# time cujo ele atua, e o número da camisa.

class Jogador:
    def __init__(self) -> None:
        self.jogador = None
        self.nome_time = None
        self.camisa = None
        
    def entrada_jogador(self) -> None:
        self.jogador = input("Digite o nome do jogador: ")
        self.nome_time = input("Digite o nome do time que ele joga: ")
        self.camisa = int(input("Digite o número da camisa: "))
        
    def saida_jogador(self) -> None:
        print(f"O nome do jogador é {self.jogador}")
        print(f"O time que ele joga é {self.nome_time}")
        print(f"O número da camisa é {self.camisa}")
        
    