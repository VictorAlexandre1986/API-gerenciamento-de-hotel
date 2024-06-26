from pydantic import BaseModel, Field
from datetime import datetime

class ContasReceberEntity(BaseModel):
    id: int 
    id_cliente:int | None
    valor: float = Field(...,decimal_places=2,max_digits=7)
    id_produto: int
    id_reserva: int
    status: str = Field(...,min_length=4)