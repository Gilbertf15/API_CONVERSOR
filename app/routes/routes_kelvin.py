from fastapi import APIRouter

from app.controller.controller_kelvin import ControllerKelvin

class RouterKelvin(APIRouter):
    def __init__(self, prefix = ""):
        super().__init__(prefix=prefix)

router_kelvin = RouterKelvin("/kelvin")


@router_kelvin.get("/get")
async def get_kelvin() -> dict | str:
    """ MÉTODO ASSINCRONO DA ROTA GET_KELVIN

    Returns:
        dict | str: Retorna o resultado do método estático get_convert() da classe ControllerKelvin
    """
    result = await ControllerKelvin.get_convert()
    return result


@router_kelvin.post("/post/{vallor}")
async def post_kelvin(valor: int | float) -> dict | str:
    """MÉTODO ASSINCRONO DA ROTA POST_KELVIN

    Args:
        valor (int | float): valor númerico esperado no argumento posicional "valor".

    Returns:
        dict | str: Retorna o resultado do método estático post_convert() da classe ControllerKelvin
    """
    result = await ControllerKelvin.post_convert(valor)
    return result


