from pydantic import BaseModel, Field
from datetime import datetime

class ReservaDTO(BaseModel):
    id: int 
    id_cliente: int   
    id_quarto: int
    qts_dias : int
    data_reserva: datetime 
    preco: float = Field(...,decimal_places=2)
