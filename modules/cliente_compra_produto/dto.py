from pydantic import BaseModel, Field
from datetime import datetime


class ClienteCompraProdutoDTO(BaseModel):
    id: int 
    id_cliente: int 
    id_produto: int
    id_reserva: int
    data: datetime
    qtd: int
        