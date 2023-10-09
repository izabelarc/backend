import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

# Uma vez criado o nosso banco de dados, temos que implementar um 'apontador'. Esse
# apontador é quem comandará o banco de dados. Como um maestro, o apontador fará  o
# acesso ao meu banco de dados e criará e manipulará as tabelas do meu banco.
# Em nosso exemplo, declararemos uma variável chamada cursor, e ele será o apontador.

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# A partir de agora, temos o maestro da nossa orquestra. O cara que fará toda a mani-
# pulação do nosso banco de dados. Ou seja, qualquer coisa que formos adicionar   ao
# banco de dados será adicionada por meio do cursos, bem como modificar, atualizar ou
# deletar. Tudo será feito pelo nosso cursor, que será chamado sempre que necessário.