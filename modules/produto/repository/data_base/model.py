from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
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
    id_fornecedor = Column(Integer, ForeignKey('tb_fornecedor.id'))
    data_validade = Column(DateTime, nullable=False)
    contas_pagar = relationship(ContasPagar, back_populates='produto')
    contas_receber = relationship(ContasReceber, back_populates='produto')