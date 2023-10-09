import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# Após inserir informações no banco de dados, é possível ler essas informações. Para isso,
# utilize o comando SELECT nome, turma, matricula FROM alunos_matriculados.
# Esse comando quer dizer o seguinte: selecione os dados das colunas nome, turma e matrícula
# do banco de dados 'alunos_matriculados'
linhas = cursor.execute("SELECT nome, turma, matricula FROM alunos_matriculados").fetchall()

# Antes de encerrar a conexão, experimente utilizar a função print() para exibir o(s) valor(es)
# atribuído(s) à variável linhas. Qual foi a saída de dados?

# Fechando a conexão com o banco de dados
conexao.close()