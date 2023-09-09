# Crie um arquivo Python exercicio09.py. Após, crie uma classe Veiculo com os seguintes
# atributos: quantidade_rodas (int), tipo_motor (str), capacidade_quilos (float),
# tipo_combustivel (str) capacidade_tanque (float), cor (str), tem_air_bag (bool) e
# velocidade_maxima (float). Após, crie funções diversas para seu veículo: acelerando,
# carregando passageiros, tanque vazio/cheio etc. Use a criatividade para criar sua classe
# veículo. Finalmente, crie duas cópias (objetos) dessa classe: veiculo1 e veiculo2 e
# teste suas funções.

class Veiculo:
    def __init__(self, quantidade_rodas:int, tipo_motor:str, capacidade_quilos:float, tipo_combustivel:str, capacidade_tanque:float, cor:str, tem_air_bag:bool, velocidade_maxima:float) -> None:
        self.quantidade_rodas = quantidade_rodas
        self.tipo_motor = tipo_motor
        self.capacidade_quilos = capacidade_quilos
        self.tipo_combustivel = tipo_combustivel
        self.capacidade_tanque = capacidade_tanque
        self.cor = cor
        self.tem_air_bag = tem_air_bag
        self.velocidade_maxima = velocidade_maxima

    def acelerando(self) -> None:
        print("O veículo está acelerando")
    def passageiros(self) -> None:
        print("O veículo está carregando passageiros")
    def tanque(self) -> None:
        print("Necessário abastecimento")
    def ficha(self) -> None:
        print("FICHA DO VEÍCULO")
        print(f"Quantidade rodas: {self.quantidade_rodas} ")
        print(f"Tipo de motor: {self.tipo_motor}")
        print(f"Capacidade do veículo: {self.capacidade_quilos}")
        print(f"Combustível: {self.tipo_combustivel}")
        print(f"Capcidade do tanque: {self.capacidade_tanque}")
        print(f"Cor: {self.cor}")
        print(f"Airbag: {self.tem_air_bag}")
        print(f"Valocidade máxima: {self.velocidade_maxima}")