# Crie um arquivo Python exercicio05.py. Após, crie uma classe Cachorro com os
# seguintes atributos: nome_popular (str), nome_cientifico (str), tempo_vida (int),
# habitat_natural (str), alimentacao (list), ameacado_extincao (bool), raca (str),
# cor_pelo (float), tamanho_pelo (float) e tem_dono (bool). Após, crie uma função
# latindo() que exiba na tela “au, au, au...”. Crie outras funções, comendo(), bebendo(),
# correndo() e dormindo(), e exiba uma mensagem para cada uma dessas funções.
# Implemente, também, uma função que mostre se o cachorro tem dono. Finalmente, crie
# duas cópias (objetos) dessa classe: cachorro1 e cachorro2.

from bibliotecas.animal import *

class Cachorro(Animal):
    def __init__(self, nome_pop:str, nome_cient:str, tempo_vida:int, habitat_natural:str, alimentacao:list,
                 ameacado_extincao:bool, raca:str, cor_pelo:str, tamanho_pelo:str, tem_dono:bool) -> None:
        super().__init__(nome_pop, nome_cient, tempo_vida, habitat_natural, alimentacao, ameacado_extincao)
        self.raca= raca
        self.cor_pelo= cor_pelo
        self.tamanho_pelo=tamanho_pelo
        self.tem_dono= tem_dono
        
    def latindo(self) -> None:
        print(f"Au, au, au...")
    def dono(self) -> None:
        if self.tem_dono == True:
            print(f"Tem dono")
        else:
            print(f"Não tem dono")
    def comendo(self) -> None:
        return super().comendo()
    def correndo(self) -> None:
        return super().comendo()
    def bebendo(self) -> None:
        return super().comendo()
    def dormindo(self) -> None:
        return super().comendo()