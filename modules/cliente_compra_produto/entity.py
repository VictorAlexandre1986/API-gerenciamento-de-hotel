from pydantic import BaseModel, Field
from datetime import datetime


class ClienteCompraProdutoEntity(BaseModel):
    id: int 
    id_cliente: int 
    id_produto: int
    qtd: int