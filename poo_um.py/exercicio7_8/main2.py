from bibliotecas.smartphone import *

smartphone1 = Smartphone(
    marca= "Apple",
    modelo= "Iphone 12",
    polegadas= 6.06,
    cor= "Preto",
    wifi= True,
    dual_chip= False,
    codigo_IMEI= 518247382177626,
    leitor_facial= True,
    leitor_digital= False, 
    tem_camera_frontal= True, 
    megapixel_camera_frontal= 12, 
    megapixel_camera_traseira= 12
)

smartphone2 = Smartphone(
    marca= "Xiaomi",
    modelo= "Redmi Note 12 Pro",
    polegadas= 6.67,
    cor= "Branco",
    wifi= False,
    dual_chip= True,
    codigo_IMEI= 335819434661665,
    leitor_facial= False,
    leitor_digital= True, 
    tem_camera_frontal= True, 
    megapixel_camera_frontal= 50, 
    megapixel_camera_traseira= 16
)

smartphone3 = Smartphone(
    marca= "Xiaomi",
    modelo= "Redmi Note 12 Pro",
    polegadas= 6.67,
    cor= "Branco",
    wifi= True,
    dual_chip= True,
    codigo_IMEI= 335819434661665,
    leitor_facial= False,
    leitor_digital= True, 
    tem_camera_frontal= False, 
    megapixel_camera_frontal= 50, 
    megapixel_camera_traseira= 16
)

smartphone1.download()
print()
smartphone2.download()
print()
smartphone3.download()