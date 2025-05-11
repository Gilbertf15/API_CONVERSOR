from fastapi import APIRouter

from app.controller.controller_libras import ControllerLibras

class RouterLibras(APIRouter):
   def __init__(self, prefix = ""):
       super().__init__(prefix=prefix)

router_quilogramas_libras = RouterLibras("/libras")

@router_quilogramas_libras.get("/get_quilogramas_libras")
async def get_quilogramas_libras() -> dict | str:
    """MÉTODO ASSINCRONO DA ROTA GET_QUILOGRAMAS

    Returns:
        dict | str: Retorna o resultado do método estático get_convert() da classe ControllerLibras
    """
    result = await ControllerLibras.get_convert()
    return result


@router_quilogramas_libras.post("/post_quilogramas_libras{valor}")
async def post_quilogramas_libras(valor: int | float) -> dict | str:
    """METODO ASSINCRONO DA ROTA POST QUILOGRAMAS

    Args:
        valor (int | float): valor númerico esperado no argumento posicional "valor".

    Returns:
        dict | str: Retorna o resultado do método estático post_convert() da classe ControllerLibras
    """
    result = await ControllerLibras.post_convert(valor)
    return result

