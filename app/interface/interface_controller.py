from abc import ABC, abstractmethod

class InterfaceController(ABC):
    """CRIAÇÃO DA INTERFACE PARA IMPLEMENTAR NOS CONTROLLERS"""

   
    @abstractmethod
    async def get_convert(self):
        """Método abstrato get para ser implementado
        """
        raise NotImplementedError('Metodo get_convert precisa ser implementado')


    @abstractmethod
    async def post_convert(self, valor):
        """Método abstrato post para ser implementado

        Args:
            valor (None): argumento posicional do método
        """
        raise NotImplementedError('Metodo post_convert precisa ser implementado em suas classes filhas.')
    