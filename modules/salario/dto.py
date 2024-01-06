from pydantic import BaseModel, Field
from datetime import datetime

class SalarioDTO(BaseModel):
    id: int 
    id_funcionario: int   
    salario:float = Field(..., decimal_places=2)
    salario_status: bool
    vale_refeicao:float =  Field(..., decimal_places=2)
    vale_refeicao_status: bool
    auxilio_medico: float = Field(..., decimal_places=2)
    auxilio_medico_status:bool
    