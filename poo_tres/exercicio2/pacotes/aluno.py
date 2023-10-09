class Aluno:
    """
    Essa é a nossa classe Aluno, uma estrutura de dados criada por nós na última aula
    a fim de resolvermos o problema com os dicionários na lista.

    Notem que nossa classe Aluno é responsável por "criar" novos alunos a partir dos
    parâmetros nome(str) e idade(int).
    """
    def __init__(self, nome: str, idade: int) -> None:
        """
        Método inicializador serve para definirmos os atributos da nossa classe.
        
        Nesse caso, temos dois atributos: nome(str) e idade(int).

        Informamos ao método __init__ que sempre que quisermos trabalhar com os
        parâmatros 'nome' e 'idade' utilizamos 'self.nome' e 'self.idade', res-
        pectivamente.

        Parâmetros:
            nome(str): nome do aluno
            idade(int): idade do aluno

        Retorno:
            None: esta função não tem retorno
        """
        self.nome = nome
        self.idade = idade
    

    def nome_aluno(self) -> str:
        """
        Esta função retorna o nome do aluno.

        Retorno:
            str: nome do aluno
        """
        return self.nome
    

    def idade_aluno(self) -> str:
        """
        Esta função retorna a idade do aluno.

        Retorno:
            int: idade do aluno
        """
        return self.idade