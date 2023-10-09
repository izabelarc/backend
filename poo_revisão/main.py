from pacotes.jogador import *
from pacotes.comissao import *
from pacotes.time import *

novo_jogador = Jogador()
novo_jogador.entrada_jogador()
novo_jogador.saida_jogador()

novo_time = Time()
novo_time.entrada_time()
novo_time.saida_time()

novo_tecnico = Comissao()
coletiva1 = Comissao()
novo_tecnico.entrada_tecnico()
novo_tecnico.saida_tecnico()
coletiva1.dar_coletiva_tec()

novo_auxiliar = Comissao()
coletiva2 = Comissao()
novo_auxiliar.entrada_auxiliar()
novo_auxiliar.saida_auxiliar()
coletiva2.dar_coletiva_aux()

novo_preparador = Comissao()
coletiva3 = Comissao()
novo_preparador.entrada_preparador()
novo_preparador.saida_preparador()
coletiva3.dar_coletiva_prep()
