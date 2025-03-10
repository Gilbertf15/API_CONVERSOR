import sqlite3
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import Connection

"""Conexão com o banco"""

 # -- --
    
CONNECTION_FAHRENHEIT  = Connection()
OBJ_CONNECTION = CONNECTION_FAHRENHEIT.get_connection()
    #-- --
CURSOR_FAHRENHEIT = OBJ_CONNECTION.cursor()

class ControllerFahrenheit(InterfaceController):
   
    @staticmethod
    async def get_convert() -> dict | str:
        """"""# função get para buscar as conversôes de Celsius para Fahrenheit
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
        """fução post para fazer uma conversão especifica de Celsius para Fahrenheit"""
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