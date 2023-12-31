from pydantic import BaseModel, Field
from datetime import datetime

class FuncionarioEntity(BaseModel):
    id: int 
    nome: str = Field(..., min_length=2) 
    cpf: str = Field(...,min_length=11,max_length=11)
    endereco: str = Field(...,min_length=5)
    bairro:str = Field(...,min_length=5)
    cidade: str = Field(...,min_length=5)
    contato:str = Field(...,min_length=10,max_length=11)
    data_nascimento:datetime 