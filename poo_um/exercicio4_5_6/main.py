# Crie um arquivo Python exercicio04.py. Após, crie uma classe Animal com os seguintes
# atributos: nome_popular (str), nome_cientifico (str), tempo_vida (int),
# habitat_natural (str), alimentacao (list) e ameacado_extincao (bool). Após, crie uma
# função status_animal() que exiba o nome popular, o nome científico e se está
# ameaçado de extinção. Crie outras funções, comendo(), bebendo(), correndo() e
# dormindo(), e exiba uma mensagem para cada uma dessas funções. Finalmente, crie
# duas cópias (objetos) dessa classe: animal1 e animal2.
# Obs.: o atributo alimentacao é uma lista que deve receber os alimentos que o animal
# pode comer. Use a criatividade ou o Google para buscar essas informações.

from bibliotecas.animal import Animal 

animal1 = Animal(
    nome_pop= "Leão",
    nome_cient= "Panthera leo",
    tempo_vida= 10,
    habitat_natural= "Savanas da África",
    alimentacao= ["gnus", "zebras", "antílopes"],
    ameacado_extincao= True
)
animal2 = Animal(
    nome_pop= "Golfinho",
    nome_cient= "Delphinus delphis",
    tempo_vida= 60,
    habitat_natural= "Ambientes marinhos",
    alimentacao= ["moluscos", "peixes", "crustáceos"],
    ameacado_extincao= True
)

animal1.status_animal()
animal2.status_animal()
animal1.comendo()
animal2.comendo()
