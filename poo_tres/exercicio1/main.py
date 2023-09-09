from database import Database as DB
from db import lista_alunos 

db = DB(lista_alunos)

# db.mostrar_cadastros()
# db.mostrar_cadastro(2)
# db.cadastrar_aluno(nome="Diana", idade="54")

db.excluir_aluno(2)