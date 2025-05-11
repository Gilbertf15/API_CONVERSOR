import sqlite3
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import Connection

"""CONEXÃO COM O BANCO"""
# -- constante de conexão com o banco --    
CONNECTION_FAHRENHEIT  = Connection()
OBJ_CONNECTION = CONNECTION_FAHRENHEIT.get_connection()

# -- constante cursor da conexão --
CURSOR_FAHRENHEIT = OBJ_CONNECTION.cursor()

class ControllerFahrenheit(InterfaceController):
    """CLASSE CONTROLLERFAHRENHEIT PARA CRIAR AS OPERAÇÔES

    Args:
        InterfaceController (ABC): Interface controller para ser implementada

    
    """
    @staticmethod
    async def get_convert() -> dict | str:
        """MÉTODO ASSINCRONO GET PARA BUSCAR AS CONVERSÕES DE CELSIUS PARA FAHRENHEIT NO BANCO

        Returns:
            dict : retornar um dicionario com as conversões de 0 a 100

            str : Retornar uma trarativa indicando um erro
        """
        try:
            CURSOR_FAHRENHEIT.execute("SELECT Celsius,fahrenheit FROM fahrenheit")
            resultado = CURSOR_FAHRENHEIT.fetchall()
            convert = resultado
            return dict(convert)

        except requests.exceptions.ConnectionError:
            return "error conection"
        
        except requests.exceptions.HTTPError  as e:
            return f"Error {e}"

      
      


    @staticmethod
    async def post_convert(valor: int | float) -> dict | str:
        """MÉTODO ASSINCRONO POST PARA FAZER UMA CONVERSÃO ESPECÍFICA DE CELSIUS PARA FAHRENHEIT

        Args:
            valor (int | float): Valor númerico esperado para ralizar a conversão 

        Returns:
            dict : Retornar um dicionario com o valor usado na conversão e o resultado da operação

            str : Retornar uma trarativa indicando um erro
        """
        if valor >  0:

            try:
                result = (valor*9/5) + 32
                return {
                    'Celsius': valor,
                    'Fahrenheit': result
                }
            
            except requests.exceptions.ConnectionError:
                return "error conection"
            
            except ValueError:
                return "Error, valor invalido"

            except:
                return "error ao solicitar post_fahrenheit"

        else:
            return "valor invalido"