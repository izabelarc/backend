from pacotes.bancodedados import BancoDeDados as DB
from pacotes.aluno import Aluno
from dados import lista_alunos as dados 

db = DB(dados)

# db.mostrar_dado(id=1)
db.adicionar_dado2(Aluno("Ana", 15))
# db.mostrar_dados()