# Crie um arquivo Python exercicio08.py. Após, crie uma classe Smartphone com os
# seguintes atributos: marca (str), modelo (str), polegadas (float), cor (str), wifi (bool),
# dual_chip (bool), codigo_IMEI (int), leitor_facial (bool), leitor_digital (bool),
# tem_camera_frontal (bool), megapixel_camera_frontal (int) e
# megapixel_camera_traseira (int). Após, crie uma função download(aplicativo: str)
# que receba como parâmetro o nome de um aplicativo. Se o Smartphone tiver Wifi,
# poderá baixar quaisquer aplicativos, exceto Instagram. Se o Smartphone tiver Wifi e o
# aplicativo informado como parâmetro for o Instagram, pode baixar somente se tiver
# câmera frontal. Finalmente, crie duas cópias (objetos) dessa classe: smartphone1 e
# smartphone2 e teste seus métodos.

from bibliotecas.celular import *

class Smartphone(Celular):
    def __init__(self, marca:str, modelo:str, polegadas:float, cor:str, wifi:bool, dual_chip:bool, codigo_IMEI:int, leitor_facial:bool,
                 leitor_digital:bool, tem_camera_frontal:bool, megapixel_camera_frontal:int, megapixel_camera_traseira:int) -> None:
        super().__init__(marca, modelo, polegadas, cor, wifi, dual_chip, codigo_IMEI)
        self.leitor_facial = leitor_facial
        self.leitor_digital=leitor_digital
        self.tem_camera_frontal= tem_camera_frontal
        self.megapixel_camera_frontal= megapixel_camera_frontal
        self.megapixel_camera_traseira=megapixel_camera_traseira

    def download(self) -> None:
        aplicativo = input("Digite o nome do aplicativo: ")
        if self.wifi == True:
            if aplicativo == "Instagram" or aplicativo == "instagram":
                if self.tem_camera_frontal == True:
                    print("O aplicativo está sendo instalado.")
                else:
                    print("O aplicativo não pode ser instalado, pois não tem câmera frontal.")
            else:
                print("O aplicativo está sendo instalado.")
        else:
            print("O aplicativo não pode ser instalado, pois não tem wifi")