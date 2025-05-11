from fastapi import FastAPI


class APICONVERT(FastAPI):
   """CRIAÇÃO DA CLASSE APICONVERT QUE HERDA DE FASTAPI

   """

   #Método construtor da API
   def __init__(self, debug = True, title = "APICONVERT", summary = None
                , description = "API para conversão de unidades", version = "0.1.0" ):
    super().__init__(debug=debug, title=title, summary=summary,
                      description=description, version=version)
    

    
    