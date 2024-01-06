from sqlalchemy import Column, Float, String, Integer, ForeignKey
from modules.produto.repository.data_base.model import Produto
from sqlalchemy.orm import relationship

from infra.db import Base

class ContasPagar(Base):
    __tablename__ = "tb_contas_pagar"
    
    
    fornecedor = Column(String)
    servico = Column(String)
    valor = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    id_produto = Column(Integer, ForeignKey('tb_produto.id'))
    produto = relationship(Produto, back_populates='tb_contas_pagar')
    