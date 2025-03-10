import sqlite3


class Connection():
    #conexão com o banco
    def __init__(self):
    
        self.__conexao = sqlite3.connect('conversao.db')
        self.__cursor_db = self.__conexao.cursor()


    #criação da tabela fahrenheit
    
    def get_cursor(self):
        return self.__cursor_db

    def get_connection(self):
        return self.__conexao


obj_connection = Connection()