from fastapi import APIRouter
from app.controller.controller_fahrenheit import ControllerFahrenheit

class RouterFahrenheit(APIRouter):
   def __init__(self, prefix = ""):
      super().__init__(prefix=prefix)
   

router_fahrenheit = RouterFahrenheit("/fahrenheit")

@router_fahrenheit.get("/get")
async def get_fahrenheit() -> dict | str:
    """ MÉTODO ASSINCRONO DA  ROTA GET_FAHRENHEIT

    Returns:
        dict | str: espera como resultado do método estático get_convert() da classe ControllerFahrenheit
    """
    result = await ControllerFahrenheit.get_convert()
    return result


@router_fahrenheit.post("/post/{valor}")
async def post_fahrenhei(valor: int | float) -> dict | str:
    """ MÉTODO ASSINCRONO  DA ROTA POST_FAHRENHEIT

    Args:
        valor (int | float): valor númerico esperado no argumento posicional "valor".

    Returns:
        dict | str: espera como resultado do método estático post_convert() da classe ControllerFahrenheit
    """
    result = await ControllerFahrenheit.post_convert(valor)
    return result


