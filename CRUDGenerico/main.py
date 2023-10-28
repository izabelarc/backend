from CRUDGenerico import CRUDGenerico as CRUD

db = CRUD(
    banco_dados="db_teste.db"
)

# db.criar_tabela(
#     nome_tabela="tabela_dois",
#     query_sql="""
#         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#         nome TEXT NOT NULL,
#         peso REAL NOT NULL,
#         idade INTEGER NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         cor_favorita TEXT NOT NULL
#     """
# )
print(db.listar_colunas("tabela_dois"))

db.inserir(
    "tabela_dois",
    "Izabela",
    85,
    23,
    "izabelainfinity@gmail.com",
    "vermelho"
)