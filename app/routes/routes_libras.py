from fastapi import APIRouter

from app.controller.controller_libras import ControllerLibras

class RouterLibras(APIRouter):
   def __init__(self, prefix = ""):
       super().__init__(prefix=prefix)

router_quilogramas_libras = RouterLibras("/libras")

@router_quilogramas_libras.get("/get_quilogramas_libras")
async def get_quilogramas_libras() -> dict | str:
    """_summary_

    Returns:
        dict | str: _description_
    """
    result = await ControllerLibras.get_convert()
    return result


@router_quilogramas_libras.post("/post_quilogramas_libras{valor}")
async def post_quilogramas_libras(valor: int | float) -> dict | str:
    """_summary_

    Args:
        valor (int | float): _description_

    Returns:
        dict | str: _description_
    """
    result = await ControllerLibras.post_convert(valor)
    return result

