from bibliotecas.gato import Gato

gato1 = Gato(
    nome_pop= "Gato",
    nome_cient= "Felis catus",
    tempo_vida= 18,
    habitat_natural= "Terrestre",
    alimentacao= ["ração", "petisco", "sache"],
    ameacado_extincao= False,
    raca="Laranja",
    cor_pelo="Laranja  branco",
    tamanho_pelo="Curto",
    tem_dono= True,
    meu_humano= "João",   
)

gato2 = Gato(
    nome_pop= "Gato",
    nome_cient= "Felis catus",
    tempo_vida= 18,
    habitat_natural= "Terrestre",
    alimentacao= ["ração", "petisco", "sache"],
    ameacado_extincao= False,
    raca="Malhado",
    cor_pelo="Preto e branco",
    tamanho_pelo="Curto",
    tem_dono= True,
    meu_humano= "Maria",
)

gato1.comendo()
gato2.comendo()
gato1.miando()
gato2.miando()
gato1.tem_humano()
gato2.tem_humano()