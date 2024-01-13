from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.salario.repository.data_base.model import Salario

from infra.db import Base

class Cliente(Base):
    __tablename__ = "tb_cliente"
    
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    dt_nasc= Column(DateTime, nullable=False)
    sexo= Column(String, nullable=False)
    endereco= Column(String, nullable=False)
    bairro= Column(String, nullable=False)
    cidade= Column(String, nullable=False)
    estado= Column(String, nullable=False)
    contato= Column(String, nullable=False)



    
    