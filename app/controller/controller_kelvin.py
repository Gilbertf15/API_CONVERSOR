import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection

"""CONEXÃO COM O BANCO"""
# -- constante de conexão com o banco --
CONNECTION_KELVIN = obj_connection.get_connection()

# -- constante cursor da conexão --
CURSOR_KELVIN  = CONNECTION_KELVIN.cursor()

class ControllerKelvin(InterfaceController):
    """CLASSE CONTROLLERKELVIN PARA CRIAR AS OPERAÇÔES

    Args:
        InterfaceController (ABC): Interface controller para ser implementada

    
    """
    
    @staticmethod
    async def get_convert() -> dict | str:
        """MÉTODO ASSINCRONO GET PARA BUSCAR AS CONVERSÕES DE CELSIUS  PARA KELVIN NO BANCO

        Returns:
            dict : retornar um dicionario com as conversões de 0 a 100

            str : Retornar uma trarativa indicando um erro
        """
        try:
            CURSOR_KELVIN.execute("SELECT Celsius,kelvin FROM kelvin")
            result = CURSOR_KELVIN.fetchall()
            convert_kelvin = result
            return dict(convert_kelvin)

        except requests.exceptions.HTTPError as e:
            return f"error {e}"
        
        except requests.exceptions.ConnectionError:
            return "error connection"
        

    @staticmethod
    async def post_convert(valor: int | float) -> dict | str:
        """MÉTODO ASSINCRONO POST PARA FAZER UMA CONVERSÃO ESPECÍFICA DE CELSIUS PARA KELVIN

        Args:
            valor (int | float): Valor númerico esperado para ralizar a conversão 

        Returns:
            dict : Retornar um dicionario com o valor usado na conversão e o resultado da operação

            str : Retornar uma trarativa indicando um erro
        """
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
        
        except requests.exceptions.HTTPError as e:
                return f"error {e}"
        
        except requests.ConnectionError:
            return "connection error"
