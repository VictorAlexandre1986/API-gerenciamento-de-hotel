from sqlalchemy import Column, Float, String, DateTime
from sqlalchemy.orm import relationship
from modules.salario.repository.data_base.model import Salario

from infra.db import Base

class Funcionario(Base):
    __tablename__ = "tb_funcionario"
    
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    endereco = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    salario = relationship(Salario, back_populates='funcionario')