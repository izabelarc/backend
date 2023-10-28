import sqlite3 as sql

class CRUDGenerico:
    def __init__(self, banco_dados: str) -> None:
        self.banco_dados = banco_dados
        self.conexao = None
        self.cursor = None
        
    def conectar(self) -> None:
        self.conexao = sql.connect(self.banco_dados)
        self.cursor = self.conexao.cursor()
        
    def listar_tabelas(self) -> None:
        self.conectar()
        lista_tabelas = []
        informacoes = self.cursor.execute(
            "SELECT * FROM sqlite_master WHERE type='table'"
        ).fetchall()
        for tabela in informacoes:
            lista_tabelas.append(tabela[1])
        
        print(lista_tabelas)
        
    def listar_colunas(self, nome_tabela: str) -> None:
        self.conectar()
        string_colunas = ""
        descricao = self.cursor.execute(f"SELECT * FROM {nome_tabela}").description
        
        for coluna in descricao[1:]:
            string_colunas = string_colunas +coluna[0] + ","
            
        return string_colunas[:-1]
        
    def criar_tabela(self, nome_tabela:str, query_sql: str) -> None:
        self.conectar()
        
        self.cursor.execute(f"CREATE TABLE {nome_tabela} ({query_sql})")
        
        self.conexao.commit()
        
    def inserir(self, nome_tabela:str, *dados:tuple[any]) -> None:
        self.conectar()
        string_colunas = self.listar_colunas(nome_tabela=nome_tabela)
        interrogacoes = "?," * (len(dados)-1)
        self.cursor.execute(
            f"INSERT INTO {nome_tabela} ({string_colunas}) VALUES ({interrogacoes}?)", dados
        )
        self.conexao.commit()
        self.conexao.close()