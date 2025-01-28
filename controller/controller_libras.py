
import sqlite3
"""Conexão com o banco"""
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()
class ControllerLibras:

    @staticmethod
    async def get_quilograamas_libras() -> dict | str:
        """# função get para buscar as conversôes de quilogramas  para libras """
        try:
            cursor_db.execute("SELECT quilogramas,libras FROM libras")
            result_libras = cursor_db.fetchall()
            convert_libras = result_libras
            return dict(convert_libras)
        
        except:
            return "error ao solicitar get_quilogramas_libras"

    @staticmethod
    async def post_quilogramas(valor: int | float) -> dict | str:
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
        
        except:
                return "error ao solicitar quilogramas_libras"
