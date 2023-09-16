from pacotes.aluno import Aluno

class BancoDeDados:
    """
    Esta é a nossa classe BancoDeDados, que será responsável por manipular
    os dados que estão armazenados na lista.  Lembre-se  que  nossa  lista
    armazena dados do tipo Aluno <class 'Aluno'>.
    """
    def __init__(self, dados: list) -> None:
        """
        Método construtor

        Args:
            dados(list): lista de dados
        
        Retorno:
            None
        """
        self.dados = dados

    
    def mostrar_dados(self) -> None:
        """
        Este método mostra todos os dados da <class 'list'> lista_alunos

        Retorno:
            None
        """
        for index, dado in enumerate(self.dados):
            print(f"ID: {index+1}")
            print(f"Nome: {dado.nome_aluno()}")
            print(f"Idade: {dado.idade_aluno()}", end='\n\n')
    

    def mostrar_dado(self, id: int) -> None:
        """
        Este método motra um dado específico a partir do seu ID

        Parâmetros:
            id(int): id do registro que será consultado

        Retorno:
            None
        """
        if id > len(self.dados):
            print(f"Cadastro ID {id} não localizado!")
        else:
            dado_buscado = self.dados[id-1]
            
            print(f"ID: {id}")
            print(f"Nome: {dado_buscado.nome_aluno()}")
            print(f"Idade: {dado_buscado.idade_aluno()}")
    

    def cadastrar_aluno(self, nome: str, idade: int) -> None:
        """
        Este método cadastra um aluno no "banco de dados"

        Parametros:
            nome(str): nome do aluno que será cadastrado
            idade(int): idade do aluno que será cadastrado
        
        Retorno:
            None
        """
        self.dados.append(Aluno(nome, idade))

        print(f"Aluno cadastrado com sucesso!", end='\n\n')

        self.mostrar_dado(len(self.dados))
