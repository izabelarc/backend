# Crie um arquivo Python exercicio07.py. Após, crie uma classe Celular com os seguintes
# atributos: marca (str), modelo (str), polegadas (float), cor (str), wifi (bool), dual_chip
# (bool) e codigo_IMEI (int). Após, crie uma função configuracoes() que exiba na tela as
# todas configurações do aparelho. Finalmente, crie duas cópias (objetos) dessa classe:
# celular1 e celular2.

class Celular:
    def __init__(self, marca:str, modelo:str, polegadas:float, cor:str, wifi:bool, dual_chip:bool, codigo_IMEI:int) -> None:
        self.marca= marca
        self.modelo=modelo
        self.polegadas=polegadas
        self.cor=cor
        self.wifi=wifi
        self.dual_chip=dual_chip
        self.codigo_IMEI=codigo_IMEI

    def configuracoes(self) -> None:
        print("CONFIGURAÇÕS DO APARELHO")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Polegadas: {self.polegadas}")
        print(f"Cor: {self.cor}")
        if self.wifi == True: 
            print(f"Wifi: Sim")
        else:
            print(f"Wifi: Não")
        if self.dual_chip == True:
            print(f"Dual chip: Sim")
        else:
            print(f"Dual chip: Não")
        print(f"Código do IMEI: {self.codigo_IMEI}")