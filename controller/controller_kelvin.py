import sqlite3
"""Conexão com o banco"""
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()
class ControllerKelvin:
    
    @staticmethod
    async def get_celsius_kelvi() -> dict | str:
        """ função get para buscar as conversôes de Celsius para Kevin """
        try:
            cursor_db.execute("SELECT Celsius,kelvin FROM kelvin")
            result = cursor_db.fetchall()
            convert_kelvin = result
            return dict(convert_kelvin)

        except:
            return "error ao solicitar get_kelvin"

    @staticmethod
    async def post_celsius_kelvin(valor: int | float) -> dict | str:
        """ função para fazer uma conversão especifica de Celsius para Kelvin"""
        try:
            if valor > 0:
                    result_kelvin = valor + 273.15
                    return {
                        'Celsius': valor,
                        'Kelvin': result_kelvin
                    }

            else:
                return "valor invalido"
        except ValueError:
                return "Error, valor invalido"
        except:
                return "error ao solicitar"