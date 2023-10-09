import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# Neste momento, temos o cursor chamando seu método .execute(). Executaremos, portanto,
# a primeira tabela do nosso banco de dados: alunos_matriculados.
# Nesta tabela, teremos quatro campos principais:

# nome         : qual o tipo de dado de nome_completo?
# turma        : qual o tipo de dado de turma?
# matricula    : qual o tipo de dado de numero_matricula?

# Antes de fazermos qualquer tipo de execução da nossa tabela, precisamos entender alguns
# termos para dizer o tipo de dado que a coluna da nossa tabela guardará. Para isso, aces-
# se o material TERMOS CRIAÇÃO DE TABELAS EM BANCO DE DADOS, disponível no Google Classroom
# da turma. Após, faça as alterações necessárias para o nosso .execute() criar a tabela.

# criando a tabela do nosso banco de dados, caso a tabela não exista (IF NOT EXISTS)
cursor.execute("CREATE TABLE IF NOT EXISTS alunos_matriculados (nome <TIPO DADO>, turma <TIPO DADO>, matricula <TIPO DADO>)")