from fastapi import APIRouter


class RouterWelcome(APIRouter):
   def __init__(self, prefix = ""):
       super().__init__(prefix=prefix)
       self.prefix = prefix


router_welcome = RouterWelcome("/welcome")

@router_welcome.get("/")
async def home_api() -> dict | str:
    """Crição de rota principal com instruções sobre a API 
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
    except:
        return "error API"


