import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# O método .cursor() possui várias funções para manipular um banco de dados. Neste ED,
# trabalharemos com o .execute(), um método que executará tudo o que for necessário
# para manipulação do nosso banco de dados. Como a variável 'cursor' recebeu todos os
# métodos do .cursor(), basta chamarmos nossa variável seguida de .execute():

cursor.execute()