# Para a comissão técnica, teremos o técnico, o auxiliar e o preparador físico

class Comissao:
    def __init__(self) -> None:
        self.tecnico = None
        self.time_tec = None
        self.esquema_tec = None
        self.auxiliar = None
        self.time_aux = None
        self.esquema_aux = None
        self.preparador = None
        self.nome_time_prep = None
        self.prepara = None
        
    # Para o técnico, o sistema deve cadastrar: O nome do técnico, o nome do time que
    # ele comanda, e o esquema tático preferido (4-3-3 ou 4-4-2 por exemplo), o técnico
    # deverá ter um método chamado dar_coletiva que retorna uma string: "O técnico
    # está dando uma coletiva de imprensa".
    def entrada_tecnico(self) -> None:
        self.tecnico = input("Digite o nome do técnico: ")
        self.time_tec = input("Digite o nome do time que ele comanda: ")
        self.esquema_tec = input("Digite o esquema favorito dele: ")
    
    def saida_tecnico(self)-> None:
        print(f"Nome do tecnico: {self.tecnico}")
        print(f"Time que comanda: {self.time_tec}")
        print(f"Esquema favorito: {self.esquema_tec}")
        
    def dar_coletiva_tec(self) -> None:
        coletiva_tec = None
        coletiva_tec = input("O técnico está dando uma coletiva? (Sim ou Não) ")
        if coletiva_tec.lower()[0] == "s":
            print("O técnico está dando uma coletiva de imprensa")
        else:
            print("O técnico não está em uma coletiva de imprensa.")
    
    # Para o auxiliar, deverá pedir os mesmos atributos 
    # e o método dar_coletiva retorna "O auxiliar está dando uma coletiva de imprensa".
    def entrada_auxiliar(self) -> None:
        self.auxiliar = input("Digite o nome do auxiliar: ")
        self.time_aux = input("Digite o nome do time que ele trabalha: ")
        self.esquema_aux = input("Digite o esquema favorito dele: ")
    
    def saida_auxiliar(self)-> None:
        print(f"Nome do auxiliar: {self.auxiliar}")
        print(f"Time que trabalha: {self.time_aux}")
        print(f"Esquema favorito: {self.esquema_aux}")
        
    def dar_coletiva_aux(self) -> None:
        coletiva_aux = None
        coletiva_aux = input("O auxiliar está dando uma coletiva? (Sim ou Não) ")
        if coletiva_aux.lower()[0] == "s":
            print("O auxiliar está dando uma coletiva de imprensa.")
        else:
            print("O auxiliar não está em uma coletiva de imprensa.")
            
    # Para o preparador físico, o sistema deverá pedir o nome do preparador, o nome do
    # time que ele prepara e, pedir qual parte do elenco ele prepara, "jogadores de linha" ou os "goleiros", 
    # deverá ter também o método dar_coletiva que retorna: "O preparador físico está dando uma coletiva de imprensa".
    
    def entrada_preparador(self) -> None:
        self.preparador = input("Digite o nome do preparador: ")
        self.nome_time_prep = input("Digite o nome do time que ele trabalha: ")
        self.prepara = input("Prepara jogadores de linha ou goleiros? ")
    
    def saida_preparador(self)-> None:
        print(f"Nome do preparador: {self.preparador}")
        print(f"Time que trabalha: {self.nome_time_prep}")
        print(f"Posição que prepara: {self.prepara}")
        
    def dar_coletiva_prep(self) -> None:
        coletiva_prep = None
        coletiva_prep = input("O preparador está dando uma coletiva? (Sim ou Não) ")
        if coletiva_prep.lower()[0] == "s":
            print("O preparador está dando uma coletiva de imprensa")
        else:
            print("O preparador não está em uma coletiva de imprensa.")