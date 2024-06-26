from pydantic import BaseModel, Field
from datetime import datetime


class ContasReceberDTO(BaseModel):
    id: int 
    id_cliente: int 
    valor: float = Field(...,decimal_places=2,max_digits=7)
    id_produto: int
    id_reserva: int
    status: str = Field(...,min_length=4)