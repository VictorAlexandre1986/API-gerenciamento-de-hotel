from pydantic import BaseModel, Field
from datetime import datetime

class CargoDTO(BaseModel):
    id: int 
    cargo: str = Field(..., min_length=2) 
