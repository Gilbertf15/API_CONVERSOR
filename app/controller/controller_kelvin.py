import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection

"""Conexão com o banco"""
# -- --
CONNECTION_KELVIN = obj_connection.get_connection()

# -- -- 
CURSOR_KELVIN  = CONNECTION_KELVIN.cursor()

class ControllerKelvin(InterfaceController):
    
    @staticmethod
    async def get_convert() -> dict | str:
        """ função get para buscar as conversôes de Celsius para Kevin """
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
        
        except requests.exceptions.HTTPError as e:
                return f"error {e}"
        
        except requests.ConnectionError:
            return "connection error"
