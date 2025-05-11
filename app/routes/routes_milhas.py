from fastapi import APIRouter

from app.controller.controller_milhas import ControllerMilhas

class RouterMilhas(APIRouter):
    def __init__(self, prefix = ""):
        super().__init__(prefix=prefix)
        self.prefix = prefix
        

router_milhas = RouterMilhas("/milhas")

@router_milhas.get("/get")
async def get_quilometros():
    """ método assincrono da rota get quilômetros

    Returns:
        Dict | String: Retorna o resultado do método estático get_convert() da classe ControllerMilhas
    """
    result = await ControllerMilhas.get_convert()
    return result


@router_milhas.post("/post")
async def post_quilometros_milhas(valor: int | float) -> dict | str:
    """MÉTODO ASSINCRONO DA ROTA POST QUIMÔMETROS

    Args:
        valor (int | float): valor númerico esperado no argumento posicional "valor"

    Returns:
        dict | str: Retorna o resultado do método estático post_convert() da classe ControllerMilhas
    """
    result = await  ControllerMilhas.post_convert(valor)

    return result


