
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection 
"""Conexão com o banco"""

# -- --
CONNECTION_LIBRAS = obj_connection.get_connection()

# -- --
CURSOR_LIBRAS = CONNECTION_LIBRAS.cursor()

class ControllerLibras(InterfaceController):

    @staticmethod
    async def get_convert() -> dict | str:
        """# função get para buscar as conversôes de quilogramas  para libras """
        try:
            CURSOR_LIBRAS.execute("SELECT quilogramas,libras FROM libras")
            result_libras = CURSOR_LIBRAS.fetchall()
            convert_libras = result_libras
            return dict(convert_libras)
        
        except requests.exceptions.ConnectionError:
            return "error connection"
        
        except requests.exceptions.HTTPError as e:
            return f"Error http {e}"

    @staticmethod
    async def post_convert(valor: int | float) -> dict | str:
        """função post para fazer uma conversão especifica de quilogramas para libras"""
        try:
            if valor > 0 :

                
                    result_libras = valor * 2.20462
                    return {
                        'Quilogramas': valor,
                        'Libras': result_libras
                    }
            else:
                return "valor invalido"           
        except ValueError:
                    return "Error, valor invalido"
        
        except requests.exceptions.ConnectionError:
            return "error connection"
        
        except requests.exceptions.HTTPError as e:
            return f"Error http {e}"
