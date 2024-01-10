from pydantic import BaseModel, Field
from datetime import datetime

class ProdutoDTO(BaseModel):
    id: int 
    nome: str = Field(..., min_length=2) 
    categoria: str = Field(...,min_length=3) 
    preco_custo:float = Field(..., decimal_places=2)
    preco_venda:float =  Field(..., decimal_places=2)
    id_fornecedor: int 
    data_validade = datetime
    