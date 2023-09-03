# Crie um arquivo Python exercicio06.py. Após, crie uma classe Gato com os seguintes
# atributos: nome_popular (str), nome_cientifico (str), tempo_vida (int),
# habitat_natural (str), alimentacao (list), ameacado_extincao (bool), raca (str),
# cor_pelo (str), tamanho_pelo (str) e meu_humano (str). Após, crie uma função
# miando() que exiba na tela “miau, miau, miau...”. Crie outras funções, comendo(), bebendo(),
# correndo(), dormindo() e ronronando(), e exiba uma mensagem para cada uma
# dessas funções. Implemente, também, uma função que mostre qual humano que o gato
# é dono. Finalmente, crie duas cópias (objetos) dessa classe: gato1 e gato2.

from bibliotecas.cachorro import *

class Gato(Cachorro):
     def __init__(self, nome_pop:str, nome_cient:str, tempo_vida:int, habitat_natural:str, alimentacao:list,
                 ameacado_extincao:bool, raca:str, cor_pelo:str, tamanho_pelo:str, tem_dono:bool, meu_humano:str) -> None:
        super().__init__(nome_pop, nome_cient, tempo_vida, habitat_natural, alimentacao, ameacado_extincao, raca, 
                         cor_pelo, tamanho_pelo, tem_dono)
        self.meu_humano= meu_humano

     def miando(self) -> None:
        print(f"Miau, miau, miau...")
     def ronronando(self) -> None:
        print(f"O gato está ronronando.")
     def tem_humano(self) -> None:
        print(f"O dono é: {self.meu_humano}")
     def comendo(self) -> None:
        return super().comendo()
     def correndo(self) -> None:
        return super().comendo()
     def bebendo(self) -> None:
        return super().comendo()
     def dormindo(self) -> None:
        return super().comendo()