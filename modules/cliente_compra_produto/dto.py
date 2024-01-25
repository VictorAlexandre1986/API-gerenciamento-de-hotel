from pydantic import BaseModel, Field
from datetime import datetime


class ClienteCompraProdutoDTO(BaseModel):
    id: int 
    id_cliente: int 
    id_produto: int
    qtd: int
        