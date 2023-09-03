from biblioteca.veiculo import *

veiculo1 = Veiculo(
    quantidade_rodas=2, 
    tipo_motor="Gasolina", 
    capacidade_quilos=166, 
    tipo_combustivel= "Gasolina", 
    capacidade_tanque=9,
    cor= "Azul", 
    tem_air_bag= False,
    velocidade_maxima= 180
)

veiculo2 = Veiculo(
    quantidade_rodas=4, 
    tipo_motor="Flex", 
    capacidade_quilos=375, 
    tipo_combustivel= "Gasolina ou Alcool", 
    capacidade_tanque=25,
    cor="Preto", 
    tem_air_bag= True,
    velocidade_maxima= 250
)

veiculo1.ficha()
print()
veiculo2.ficha()