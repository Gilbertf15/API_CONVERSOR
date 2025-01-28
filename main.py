from fastapi import FastAPI, requests
import uvicorn
from controller.controller_fahrenheit import ControllerFahrenheit
from controller.controller_kelvin import ControllerKelvin
from controller.controller_libras import ControllerLibras
from controller.controller_milhas import ControllerMilhas

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
async def get_fahrenheit() -> dict | str:
    result = await ControllerFahrenheit.get_celsius_fahrenheit()
    return result
    

    
@app.post("/post_fahrenheit/{valor}")
async def post_fahrenhei(valor: int | float) -> dict | str:
    result = await ControllerFahrenheit.post_celsius_fahrenheit(valor)
    return result


@app.get("/get_celsius_kelvin")
async def get_kelvin() -> dict | str:
    result = await ControllerKelvin.get_celsius_kelvi()
    return result


@app.post("/post_kelvin/{valor}")
async def post_kelvin(valor: int | float) -> dict | str:
    result = await ControllerKelvin.post_celsius_kelvin(valor)
    return result


@app.get("/get_quilogramas_libras")
async def get_quilogramas() -> dict | str:
    result = await ControllerLibras.get_quilograamas_libras()
    return result


@app.post("/quilogramas_libras/{valor}")
async def post_quilogramas_libras(valor: int | float) -> dict | str:
    result = await ControllerLibras.post_quilogramas(valor)
    return result


@app.get("/get_quilometros_mihas")
async def get_quilometros():
    result = await ControllerMilhas.get_quilometros_milhas()
    return result


@app.post("/quilometros_milhas/{valor}")
async def post_quilometros_milhas(valor: int | float) -> dict | str:
    result = await  ControllerMilhas.post_quilometros(valor)
    return result


if __name__ == '__main__':
    uvicorn.run(app, port=8000)