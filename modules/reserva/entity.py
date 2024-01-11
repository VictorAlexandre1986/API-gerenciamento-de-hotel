from pydantic import BaseModel, Field
from datetime import datetime

class EntityDTO(BaseModel):
    id: int 
    id_cliente: int   
    qts_quartos: int
    qts_dias : int
    data_reserva: datetime 
    preco: float = Field(...,decimal_places=2)