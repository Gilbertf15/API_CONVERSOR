from fastapi import APIRouter

from app.controller.controller_milhas import ControllerMilhas

class RouterMilhas(APIRouter):
    def __init__(self, prefix = ""):
        super().__init__(prefix=prefix)
        self.prefix = prefix
        

router_milhas = RouterMilhas("/milhas")

@router_milhas.get("/get")
async def get_quilometros():
    """_summary_

    Returns:
        _type_: _description_
    """
    result = await ControllerMilhas.get_convert()
    return result


@router_milhas.post("/post")
async def post_quilometros_milhas(valor: int | float) -> dict | str:
    """_summary_

    Args:
        valor (int | float): _description_

    Returns:
        dict | str: _description_
    """
    result = await  ControllerMilhas.post_convert(valor)

    return result


