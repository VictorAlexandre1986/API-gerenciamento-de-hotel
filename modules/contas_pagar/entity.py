from pydantic import BaseModel, Field

class ContasPagarDTO(BaseModel):
    id: int 
    fornecedor: str = Field(..., min_length=2) | None
    servico: str = Field(...,min_length=2) | None
    id_produto: int
    valor: float = Field(...,decimal_places=2,max_digits=7)
    status: str = Field(...,min_length=4)
    data: str