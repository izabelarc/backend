import sqlite3 as sql

# Variável de conexão
conexao = sql.connect("bancodedados.db")

# Variável apontador
cursor = conexao.cursor()

# Consulta por ID ao banco de dados
dado = cursor.execute("SELECT nome, idade FROM pessoas WHERE id = ?", (3,)).fetchall()

# Exibindo o ID conultado
print(dado)

# Encerrando a conexão com o banco
conexao.close()