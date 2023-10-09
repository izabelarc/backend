import sqlite3 as sql # importação do módulo sqlite3 como sql

conexao = sql.connect("cadastro_alunos.db") # iniciando a conexão do banco de dados

cursor = conexao.cursor() # declaração do nosso apontador 'cursor'

# Exercício:
#
# Faça um programa que pergunte ao usuário se ele deseja inserir informações no banco de dados.
# Caso afirmativo, pergunte quantos cadastros o cliente deseja inserir. Após, enquanto o número
# de registros informados não for satisfeito, peça que o usuário informe o nome,  a  turma  e a
# matrícula. Ao final, pergunte ao usuário se ele deseja exibir as informações cadastradas. Se
# sim, exiba as informações. Se não, exiba a mensagem: Dados cadastrados com sucesso. Utilize o
# espaço abaixo para desenvolver o exercício.















# Encerrando a conexão com o banco de dados
conexao.close()