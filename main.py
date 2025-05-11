from app.routes.routes_fahrenheit import router_fahrenheit
from app.routes.routes_kelvin import router_kelvin
from app.routes.routes_libras import router_quilogramas_libras
from app.routes.routes_milhas import router_milhas
import requests

from app.main.main_api import APICONVERT, FastAPI
import uvicorn

class MainRoutes:
    """classe MAin da api
    """
    @staticmethod
    def main_include_routes(app=FastAPI):
        """ método para incluir as rotas 

        Args:
            app (FastAAPI): Instância de FastAPI

        """
        app.include_router(router_fahrenheit)
        app.include_router(router_kelvin)
        app.include_router(router_quilogramas_libras)
        app.include_router(router_milhas)
       

app = APICONVERT()
@app.get("/")
async def home_api() -> dict | str:
    """Crição da rota home com instruções sobre a API 
    """
    try:
        return {
            '[GET]: Home': 'Bem Vindos a API DE CONVERCÃO DE TEMPERATURA, QUILOGRAMAS E QUILÔMETROS',
            '[GET]: /fahrenheit/get': 'Para solicitar os valores de 0 a 100 convertidos de CELSIUS para FAHRENHEIT',
            '[POST]: /fahrenheit/post/valor': 'Para buscar uma conversão específica de CELSIUS para FAHRENHEIT',
            '[GET]: /kelvin/get': 'Para solicitar os valores de 0 a 100 convertidos de CELSIUS para KELVIN',
            '[POST]: /kelvin/post/valor': 'Para buscar uma conversão específica de CELSIUS para KELVIN',
            '[GET]: /Libras/get_quilogramas_libras': 'Para solicitar os valores de 0 a 100 convertidos de QUILOGRAMAS para LIBRAS',
            '[POST]: /Libras/post_quilogramas_libras/valor': 'Para buscar uma conversão específica de QUILOGRAMAS para LIBRAS',
            '[GET]: /quilometros_mihas/get': 'Para solicitar os valores de 0 a 100 convertidos de QUILOMETROS para MILHAS',
            '[POST]: /quilometros_milhas/post/valor': 'Para buscar uma conversão específica de QUILOMETROS para MILHAS'
        }
    except requests.exceptions.HTTPError as e:
        return f"error API {e}"
    
    except requests.exceptions.ConnectionError:
        return "Error connection"

MainRoutes.main_include_routes(app)

 
if __name__ == '__main__':
    uvicorn.run(app, port=8000)