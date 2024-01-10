from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.funcionario.repository.data_base.model import Funcionario

from infra.db import Base

class Cargo(Base):
    __tablename__ = "tb_cargo"
    
    cargo = Column(String, nullable=False)
    funcionario = relationship(Funcionario, back_populates='cargo')