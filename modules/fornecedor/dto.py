from pydantic import BaseModel, Field

class FornecedorDTO(BaseModel):
    id: int 
    fornecedor: str = Field(..., min_length=2) | None
    cnpj: str = Field(...,min_length=2) | None
    contato: str = Field(...,min_length=11)
