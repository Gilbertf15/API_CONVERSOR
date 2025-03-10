from fastapi import APIRouter
from app.controller.controller_fahrenheit import ControllerFahrenheit

class RouterFahrenheit(APIRouter):
   def __init__(self, prefix = ""):
      super().__init__(prefix=prefix)
   

router_fahrenheit = RouterFahrenheit("/fahrenheit")

@router_fahrenheit.get("/get")
async def get_fahrenheit() -> dict | str:
    """_summary_

    Returns:
        dict | str: _description_
    """
    result = await ControllerFahrenheit.get_convert()
    return result


@router_fahrenheit.post("/post/{valor}")
async def post_fahrenhei(valor: int | float) -> dict | str:
    """_summary_

    Args:
        valor (int | float): _description_

    Returns:
        dict | str: _description_
    """
    result = await ControllerFahrenheit.post_convert(valor)
    return result


