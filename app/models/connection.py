import sqlite3


class Connection():
    """CLASSE DE CONEXÃO COM O BANCO DE DADOS

    """
    #Método construtor da conexão com o banco
    def __init__(self):
    
        self.__conexao = sqlite3.connect('conversao.db')
        self.__cursor_db = self.__conexao.cursor()


    # Metodo para retornar o atributo self.__cursor_db
    def get_cursor(self):
        return self.__cursor_db

    # Método para retornar o atributo self.__conexao
    def get_connection(self):
        return self.__conexao


obj_connection = Connection()