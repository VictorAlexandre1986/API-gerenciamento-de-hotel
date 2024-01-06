from sqlalchemy import Column, Float, String, DateTime, Integer, ForeignKey
from modules.produto.repository.data_base.model import Produto
from sqlalchemy.orm import relationship

from infra.db import Base

class ContasReceber(Base):
    __tablename__ = "tb_contas_receber"
    
    cliente = Column(String, nullable=False)
    vencimento = Column(DateTime, nullable=False)
    valor = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    id_produto = Column(Integer, ForeignKey('tb_funcionario.id'))
    funcionario = relationship(Produto, back_populates='tb_contas_receber')
    