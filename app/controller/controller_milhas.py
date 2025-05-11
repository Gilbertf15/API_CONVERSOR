
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection

"""CONEXÃO COM O BANCO"""
# -- constante de conexão com o banco --
CONNECTION_LIBRAS = obj_connection.get_connection()

# -- constante cursor da conexão --
CURSOR_MILHAS = CONNECTION_LIBRAS.cursor()

class ControllerMilhas(InterfaceController):
    """ CLASSE CONTROLLERMILHAS PARA CRIAR AS OPERAÇÔES

    Args:
        InterfaceController (ABC): Interface controller para ser implementada

    """
    @staticmethod
    async def get_convert() -> dict | str:
    
        """MÉTODO ASSINCRONO GET PARA BUSCAR AS CONVERSÕES DE QUILOMETROS  PARA MILHAS NO BANCO

        Returns:
            dict : retornar um dicionario com as conversões de 0 a 100

            str : Retornar uma trarativa indicando um erro
        """
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
        """FUNÇÃO POST PARA FAZER UMA CONVERSÃO ESPECÍFICA DE QUILOMETROS PARA MILHAS

        Args:
            valor (int | float): Valor númerico esperado para ralizar a conversão 

        Returns:
            dict : Retorna um dicionario com o valor usado na conversão e o resultado da operação

            str : Retorna uma trarativa indicando um erro
        """
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
