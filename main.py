from fastapi import FastAPI, requests
import uvicorn
import sqlite3
"""Conexão com o banco"""
conexao = sqlite3.connect('conversao.sqlite')

cursor_db = conexao.cursor()



#criando api
app = FastAPI()

"""Crição das rotas e suas respectivas funçôes"""  
@app.get("/")
def home_api() -> dict | str:
    """Crição de rota principal com instruções sobre a API 
    """
    try:
        return {
            '[GET]: Home': 'Bem Vindos a API DE CONVERCÃO DE TEMPERATURA, QUILOGRAMAS E QUILÔMETROS',
            '[GET]: /get_celsius_fahrenheit': 'Para solicitar os valores de 0 a 100 convertidos de CELSIUS para FAHRENHEIT',
            '[POST]: /post_fahrenheit/valor': 'Para buscar uma conversão específica de CELSIUS para FAHRENHEIT',
            '[GET]: /get_celsius_kelvin': 'Para solicitar os valores de 0 a 100 convertidos de CELSIUS para KELVIN',
            '[POST]: /post_kelvin/valor': 'Para buscar uma conversão específica de CELSIUS para KELVIN',
            '[GET]: /get_quilogramas_libras': 'Para solicitar os valores de 0 a 100 convertidos de QUILOGRAMAS para LIBRAS',
            '[POST]: /quilogramas_libras/valor': 'Para buscar uma conversão específica de QUILOGRAMAS para LIBRAS',
            '[GET]: /get_quilometros_mihas': 'Para solicitar os valores de 0 a 100 convertidos de QUILOMETROS para MILHAS',
            '[POST]: /quilometros_milhas/valor': 'Para buscar uma conversão específica de QUILOMETROS para MILHAS'
        }
    except:
        return "error API"


@app.get("/get_celsius_fahrenheit")
async def get_celsius_fahrenheit() -> dict | str:
    """"""# função get para buscar as conversôes de Celsius para Fahrenheit
    try:
        cursor_db.execute("SELECT Celsius,fahrenheit FROM fahrenheit")
        resultado = cursor_db.fetchall()
        convert = resultado
        return dict(convert)

    except:
        return "error ao solicitar get_fahrenheit"
    



@app.post("/post_fahrenheit/{valor}")
async def post_celsius_fahrenheit(valor:int | float) -> dict | str:
    """fução post para fazer uma conversão especifica de Celsius para Fahrenheit"""
    if valor >  0:

        try:
            result = (valor*9/5) + 32
            return {
                'Celsius': valor,
                'Fahrenheit': result
            }
        
        except ValueError:
            return "Error, valor invalido"

        except:
            return "error ao solicitar post_fahrenheit"

    else:
        return "valor invalido"



@app.get("/get_celsius_kelvin")
async def get_celsius_kelvi() -> dict | str:
    """ função get para buscar as conversôes de Celsius para Kevin """
    try:
        cursor_db.execute("SELECT Celsius,kelvin FROM kelvin")
        result = cursor_db.fetchall()
        convert_kelvin = result
        return dict(convert_kelvin)

    except:
        return "error ao solicitar get_kelvin"



@app.post("/post_kelvin/{valor}")
async def post_celsius_kelvin(valor: int | float) -> dict | str:
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
    except:
            return "error ao solicitar"


@app.get("/get_quilogramas_libras")
async def get_quilograamas_libras() -> dict | str:
    """# função get para buscar as conversôes de quilogramas  para libras """
    try:
        cursor_db.execute("SELECT quilogramas,libras FROM libras")
        result_libras = cursor_db.fetchall()
        convert_libras = result_libras
        return dict(convert_libras)
    
    except:
        return "error ao solicitar get_quilogramas_libras"
    


@app.post("/quilogramas_libras/{valor}")
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

    



@app.get("/get_quilometros_mihas")
async def get_quilometros_milhas() -> dict | str:
    """função get para buscar as conversôes de quilometros para milhas"""
    try:
        cursor_db.execute("SELECT quilometros,milhas FROM milhas")
        result_milhas = cursor_db.fetchall()
        convert_milhas = result_milhas
        return dict(convert_milhas)
    except:
        return "error ao solicitar get_quilometros_milhas"



@app.post("/quilometros_milhas/{valor}")
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
        

if __name__ == '__main__':
    uvicorn.run(app, port=8000)