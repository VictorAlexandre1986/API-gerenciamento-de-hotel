from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from modules.contas_pagar.repository.data_base.model import ContasPagar
from modules.contas_receber.repository.data_base.model import ContasReceber

from infra.db import Base

class Produto(Base):
    __tablename__ = "tb_produto"
    
    
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    custo_compra = Column(Float, nullable=False)
    custo_venda = Column(Float, nullable=False)
    fornecedor = Column(String, nullable=False)
    data_validade = Column(DateTime, nullable=False)
    contas_pagar = relationship(ContasPagar, back_populates='produto')
    contas_receber = relationship(ContasReceber, back_populates='produto')