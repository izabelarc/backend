# Crie um arquivo Python exercicio04.py. Após, crie uma classe Animal com os seguintes
# atributos: nome_popular (str), nome_cientifico (str), tempo_vida (int),
# habitat_natural (str), alimentacao (list) e ameacado_extincao (bool). Após, crie uma
# função status_animal() que exiba o nome popular, o nome científico e se está
# ameaçado de extinção. Crie outras funções, comendo(), bebendo(), correndo() e
# dormindo(), e exiba uma mensagem para cada uma dessas funções. Finalmente, crie
# duas cópias (objetos) dessa classe: animal1 e animal2.
# Obs.: o atributo alimentacao é uma lista que deve receber os alimentos que o animal
# pode comer. Use a criatividade ou o Google para buscar essas informações.
from random import choice
class Animal:
    def __init__(self, nome_pop:str, nome_cient:str, tempo_vida:int, habitat_natural:str, alimentacao:list, ameacado_extincao:bool) -> None:
        '''
        Método inicializador
        '''
        self.nome_pop = nome_pop
        self.nome_cient = nome_cient
        self.tempo_vida = tempo_vida
        self.habitat_natural = habitat_natural
        self.alimentacao = alimentacao
        self.ameacado_extincao = ameacado_extincao
        
    def status_animal(self) -> None:
        print("STATUS DO ANIMAL")
        print(f"Nome popular: {self.nome_pop}")
        print(f"Nome cientifico: {self.nome_cient}")
        print(f"Ameaçado de extinção: {self.ameacado_extincao}")
        
    def comendo(self) -> None:
        print(f"O animal está comendo {choice(self.alimentacao)}.")
        
    def correndo(self) -> None:
        print(f"O animal está correndo.")
        
    def bebendo(self) -> None:
        print(f"O animal está bebendo.")
        
    def dormindo(self) -> None:
        print(f"O animal está dormindo.")