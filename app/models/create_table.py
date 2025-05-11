
from connection import Connection, obj_connection


class CreateTable():
    """CLASSE PARA CRIAÇÃO DAS TABELAS NO BANCO conversao.db
    """
    
    #Método estático para criação da tabela kelvin
    @staticmethod
    def table_celsius_fahrenheit(cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS fahrenheit(id INTEGER PRIMARY KEY AUTOINCREMENT, Celsius VARCHAR(50),fahrenheit VARCHAR(50) )"
                        
        )
        connection.commit()
        connection.close()
        

    
    #Metodo estático para criação da tabela kelvin
    @staticmethod
    def table_celsius_kelvin(cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS kelvin(id INTEGER PRIMARY KEY AUTOINCREMENT,Celsius VARCHAR(50) NOT NULL,kelvin VARCHAR(50) NOT NULL )"
                        
        )
        connection.commit()
        connection.close()

    

    #Método estático para criação da tabele libras
    @staticmethod
    def table_quilogramas_libras(cursor,connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS libras(id INTEGER PRIMARY KEY AUTOINCREMENT,quilogramas VARCHAR(50) NOT NULL,libras VARCHAR(50) NOT NULL )"
                        
        )
        connection.commit()
        connection.close()
    

    #Método estático para criação da tabela milhas
    @staticmethod
    def table_quilometros_milhas(cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS milhas(id INTEGER PRIMARY KEY AUTOINCREMENT,quilometros VARCHAR(50) NOT NULL,milhas VARCHAR(50) NOT NULL )"
                        
        )
        connection.commit()
        connection.close()