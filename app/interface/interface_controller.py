from abc import ABC, abstractmethod

class InterfaceController(ABC):
    """_summary_"""

   
    @abstractmethod
    async def get_convert(self):
        """_summary_
        """
        raise NotImplementedError('Metodo get_convert precisa ser implementado')


    @abstractmethod
    async def post_convert(self, valor):
        """_summary_

        Args:
            valor (_type_): _description_
        """
        raise NotImplementedError('Metodo post_convert precisa ser implementado em suas classes filhas.')
    