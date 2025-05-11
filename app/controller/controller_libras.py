
import requests
from app.interface.interface_controller import InterfaceController
from app.models.connection import obj_connection 

"""CONEXÃO COM O BANCO"""
# -- constante de conexão com o banco --
CONNECTION_LIBRAS = obj_connection.get_connection()

# -- constante cursor da conexão --
CURSOR_LIBRAS = CONNECTION_LIBRAS.cursor()

class ControllerLibras(InterfaceController):
    """CLASSE CONTROLLERLIBRAS PARA CRIAR AS OPERAÇÔES

    Args:
        InterfaceController (ABC): Interface controller para ser implementada

    
    """
    @staticmethod
    async def get_convert() -> dict | str:

        """MÉTODO ASSINCRONO GET PARA BUSCAR AS CONVERSÕES DE QUILOGRAMAS  PARA LIBRAS NO BANCO

        Returns:
            dict : retornar um dicionario com as conversões de 0 a 100

            str : Retornar uma trarativa indicando um erro
        """
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
        """MÉTODO ASSINCRONO POST PARA FAZER UMA CONVERSÃO ESPECÍFICA DE QUILOGRAMAS PARA LIBRAS

        Args:
            valor (int | float): Valor númerico esperado para ralizar a conversão 

        Returns:
            dict : Retornar um dicionario com o valor usado na conversão e o resultado da operação

            str : Retornar uma trarativa indicando um erro
        """
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
