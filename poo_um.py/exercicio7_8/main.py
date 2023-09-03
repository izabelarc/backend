from bibliotecas.celular import *

celular1 = Celular(
    marca= "Apple",
    modelo= "Iphone 12",
    polegadas= 6.06,
    cor= "Preto",
    wifi= True,
    dual_chip= False,
    codigo_IMEI= 518247382177626
)

celular2 = Celular(
    marca= "Xiaomi",
    modelo= "Redmi Note 12 Pro",
    polegadas= 6.67,
    cor= "Branco",
    wifi= True,
    dual_chip= True,
    codigo_IMEI= 335819434661665
)

celular1.configuracoes()
print("----------------------------------------")
celular2.configuracoes()