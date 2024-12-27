import sqlite3

#conexão com o banco
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()

#criação da tabela fahrenheit
def table_celsius_fahrenheit():
    cursor_db.execute("CREATE TABLE IF NOT EXISTS fahrenheit(id INTEGER PRIMARY KEY AUTOINCREMENT, Celsius VARCHAR(50),fahrenheit VARCHAR(50) )"
                      
    )
    conexao.commit()
    

table_celsius_fahrenheit()

#criação da tabela kelvin
def table_celsius_kelvin():
     cursor_db.execute("CREATE TABLE IF NOT EXISTS kelvin(id INTEGER PRIMARY KEY AUTOINCREMENT,Celsius VARCHAR(50) NOT NULL,kelvin VARCHAR(50) NOT NULL )"
                      
    )
conexao.commit()

table_celsius_kelvin()

#criação da tabele libras
def table_quilogramas_libras():
      cursor_db.execute("CREATE TABLE IF NOT EXISTS libras(id INTEGER PRIMARY KEY AUTOINCREMENT,quilogramas VARCHAR(50) NOT NULL,libras VARCHAR(50) NOT NULL )"
                      
    )
conexao.commit()

table_quilogramas_libras()

#criação da tabela milhas
def table_quilometros_milhas():
      cursor_db.execute("CREATE TABLE IF NOT EXISTS milhas(id INTEGER PRIMARY KEY AUTOINCREMENT,quilometros VARCHAR(50) NOT NULL,milhas VARCHAR(50) NOT NULL )"
                      
    )
conexao.commit()

table_quilometros_milhas()

conexao.close()