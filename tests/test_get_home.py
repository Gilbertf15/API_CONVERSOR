from main import app
from fastapi.testclient import TestClient

client =  TestClient(app)


def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
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
    
