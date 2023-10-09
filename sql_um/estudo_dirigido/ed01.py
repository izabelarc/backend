# Inicialmente, importaremos o módulo sqlite3 para o nosso arquivo Python

import sqlite3 as sql

# No que, após a importação (import sqlite3) foi informado ao Python que
# esse módulo será importado como (as) sql. Isso é um recurso poderoso do
# Python que nos ajuda a simplificar algumas coisas. Nesse caso, ao invés
# de chamarmos o sqlite3 chamaremos apenas sql, simplificando a escrita.

# Definição de variável 'conexao' para receber o módulo sqlite3. Para isso,
# além de chamarmos o módulo sql e a função connect(), devemos informar à
# função connect() o nome do banco de dados como parâmetro:

conexao = sql.connect("cadastro_alunos.db")

# Para facilitar nosso trabalho, a função connect() cria o bando de dados
# automaticamente, caso ele não exista. Mas e se o banco de dados existir,
# o que você acredita que acontecerá ao executar o código novamente?
# R: