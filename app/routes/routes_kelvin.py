from fastapi import APIRouter

from app.controller.controller_kelvin import ControllerKelvin

class RouterKelvin(APIRouter):
    def __init__(self, prefix = ""):
        super().__init__(prefix=prefix)

router_kelvin = RouterKelvin("/kelvin")


@router_kelvin.get("/get")
async def get_kelvin() -> dict | str:
    """_summary_

    Returns:
        dict | str: _description_
    """
    result = await ControllerKelvin.get_convert()
    return result


@router_kelvin.post("/post/{vallor}")
async def post_kelvin(valor: int | float) -> dict | str:
    """_summary_

    Args:
        valor (int | float): _description_

    Returns:
        dict | str: _description_
    """
    result = await ControllerKelvin.post_convert(valor)
    return result


