import sqlite3
"""Conexão com o banco"""
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()
class ControllerFahrenheit:
    
    @staticmethod
    async def get_celsius_fahrenheit() -> dict | str:
        """"""# função get para buscar as conversôes de Celsius para Fahrenheit
        try:
            cursor_db.execute("SELECT Celsius,fahrenheit FROM fahrenheit")
            resultado = cursor_db.fetchall()
            convert = resultado
            return dict(convert)

        except:
            return "error ao solicitar get_fahrenheit"

    @staticmethod
    async def post_celsius_fahrenheit(valor: int | float) -> dict | str:
        """fução post para fazer uma conversão especifica de Celsius para Fahrenheit"""
        if valor >  0:

            try:
                result = (valor*9/5) + 32
                return {
                    'Celsius': valor,
                    'Fahrenheit': result
                }
            
            except ValueError:
                return "Error, valor invalido"

            except:
                return "error ao solicitar post_fahrenheit"

        else:
            return "valor invalido"