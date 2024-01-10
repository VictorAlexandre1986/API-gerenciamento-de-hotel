from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.fornecedor.repository.data_base.model import Produto

from infra.db import Base

class Fornecedor(Base):
    __tablename__ = "tb_fornecedor"
    
    fornecedor = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    produto = relationship(Produto, back_populates='fornecedor')