from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class Sexo(str, Enum):
    MASCULINO = "M"
    FEMENINO = "F"

class ClienteDTO(BaseModel):
    id: int 
    nome:  str = Field(..., min_length=3)    
    cpf: str
    dt_nasc : datetime
    sexo: Sexo
    endereco: str = Field(..., min_length=5) 
    bairro: str = Field(..., min_length=5) 
    cidade: str = Field(..., min_length=3) 
    estado: float = Field(...,min_length=2)
    contato: str = Field(..., min_length=10, max_length=11)