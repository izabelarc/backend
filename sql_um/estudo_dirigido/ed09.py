import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'


""" ATUALIZANDO INFORMAÇÕES DO BANCO DE DADOS """
# Imagine que seu usuário cadastrou o nome de um aluno incorretamente. Ou, a turma, ou a matrícula...
# Por essa razão, além de inserirmos informações no banco de dados e/ou ler essas informações, é fun-
# damental que o usuário tenha a possibilidade de atualizar essas informações sempre que possível.
# Assim, atualizaremos um dos dados do nosso banco por meio do comando UPDATE.

nova_matricula = 111111
nome_referencia = 'Gabriel'

# Para atualizar as informações do banco de dados, utilizamos o seguinte padrão:
cursor.execute(f"UPDATE alunos_matriculados SET matricula = ? WHERE nome = ?", (nova_matricula, nome_referencia))

# Note que sempre informamos o comando que será executado no banco de dados. Em nosso caso, UPDATE. Após, o nome da
# tabela do banco de dados que sofrerá alterações, seguido dos novos valores que serão atualizados na tabela.    Ao
# final, informamos os valores que serão inseridos no banco de dados.

# Encerrando a conexão com o banco de dados
conexao.close()