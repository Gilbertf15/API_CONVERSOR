
import sqlite3
"""Conexão com o banco"""
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()
class ControllerMilhas:

    @staticmethod
    async def get_quilometros_milhas() -> dict | str:
        """função get para buscar as conversôes de quilometros para milhas"""
        try:
            cursor_db.execute("SELECT quilometros,milhas FROM milhas")
            result_milhas = cursor_db.fetchall()
            convert_milhas = result_milhas
            return dict(convert_milhas)
        except:
            return "error ao solicitar get_quilometros_milhas"

    @staticmethod
    async def post_quilometros(valor: int | float) -> dict | str:
        """função post para fazer uma conversão especifica de quilometros para milhas"""
        try:
            if valor > 0:

            
                    result_milhas = valor * 0.621371
                    return {
                        'Quilometros':valor,
                        'milhas': result_milhas
                    }
        
            else:
                return "valor invalido"
        except ValueError:
            return "Error, valor invalido"
        except:
            return "error ao solicitar quilometros_milhas"
            
