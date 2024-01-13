from pydantic import BaseModel, Field


class TipoPagamentoDTO(BaseModel):
    id: int 
    tipo_pagamento: str = Field(...,min_length=5)
    