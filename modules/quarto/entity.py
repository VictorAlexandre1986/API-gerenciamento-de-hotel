from pydantic import BaseModel, Field
from datetime import datetime

    
class QuartoEntity(BaseModel):
    id :int
    tipo: str = Field(..., min_length=2)
    preco_aluguel : float = Field(..., decimal_places=2)
    alugado: bool = Field(..., default=False)