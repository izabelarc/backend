# Crie um arquivo Python exercicio05.py. Após, crie uma classe Cachorro com os
# seguintes atributos: nome_popular (str), nome_cientifico (str), tempo_vida (int),
# habitat_natural (str), alimentacao (list), ameacado_extincao (bool), raca (str),
# cor_pelo (float), tamanho_pelo (float) e tem_dono (bool). Após, crie uma função
# latindo() que exiba na tela “au, au, au...”. Crie outras funções, comendo(), bebendo(),
# correndo() e dormindo(), e exiba uma mensagem para cada uma dessas funções.
# Implemente, também, uma função que mostre se o cachorro tem dono. Finalmente, crie
# duas cópias (objetos) dessa classe: cachorro1 e cachorro2.

from bibliotecas.cachorro import Cachorro

cachorro1 = Cachorro(
    nome_pop= "Cachorro",
    nome_cient= "Canis lupus familiaris",
    tempo_vida= 12,
    habitat_natural= "Terrestre",
    alimentacao= ["ração"],
    ameacado_extincao= False,
    raca="Golden",
    cor_pelo="Dourado",
    tamanho_pelo="Longo",
    tem_dono= True
    
)
cachorro2 = Cachorro(
    nome_pop= "Cachorro",
    nome_cient= "Canis lupus familiaris",
    tempo_vida= 16,
    habitat_natural= "Terrestre",
    alimentacao= ["ração"],
    ameacado_extincao= False,
    raca="Yorkshire",
    cor_pelo="Dourado",
    tamanho_pelo="Curto",
    tem_dono= True
)

