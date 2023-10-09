import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# criando a tabela do nosso banco de dados, caso a tabela não exista (IF NOT EXISTS)
cursor.execute("CREATE TABLE IF NOT EXISTS alunos_matriculados (nome TEXT, turma TEXT, matricula INTEGER)")

# Após a criação da tabela, varemos a inserção dos primeiros dados. Para isso, utilizaremos
# o INSERT para inserir novos dados da tabela. Veja o exemplo do código abaixo:
#
cursor.execute("INSERT INTO alunos_matriculados VALUES ('Gabriel', '8º ano', 123095)")

# Após definir os dados que serão inseridos, precisamos confirmar a gravação dos dados no banco.
# Para isso, utilizaremos o método .commit(), que salvará as informações em nosso banco de dados.
conexao.commit()

# Lembre-se: é fundamental usar o comando .commit() após modificações no banco de dados!

# Finalmente, encerraremos a conexão com o banco de dados.
conexao.close()