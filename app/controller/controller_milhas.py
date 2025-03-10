
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection
"""Conexão com o banco"""

# -- --
CONNECTION_LIBRAS = obj_connection.get_connection()

# -- --
CURSOR_MILHAS = CONNECTION_LIBRAS.cursor()

class ControllerMilhas(InterfaceController):

    @staticmethod
    async def get_convert() -> dict | str:
        """função get para buscar as conversôes de quilometros para milhas"""
        try:
            CURSOR_MILHAS.execute("SELECT quilometros,milhas FROM milhas")
            result_milhas = CURSOR_MILHAS.fetchall()
            convert_milhas = result_milhas
            return dict(convert_milhas)
        
        except requests.exceptions.ConnectionError:
            return "error connection"
        
        except requests.exceptions.HTTPError as e:
            return  f"Error http {e}"

    @staticmethod
    async def post_convert(valor: int | float) -> dict | str:
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
        
        except requests.exceptions.ConnectionError:
            return "error connection"
        
        except requests.exceptions.HTTPError as e:
            return f"Error http {e}"
