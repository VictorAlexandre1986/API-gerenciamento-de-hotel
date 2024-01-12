from sqlalchemy import Column, Float, String, DateTime, Integer, ForeignKey
from modules.produto.repository.data_base.model import Produto
from sqlalchemy.orm import relationship

from infra.db import Base

class ContasReceber(Base):
    __tablename__ = "tb_contas_receber"
    
    valor = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    id_cliente = Column(String, ForeignKey('tb_cliente'))
    id_produto = Column(Integer, ForeignKey('tb_funcionario.id'))
    id_reserva = Column(Integer, ForeignKey('tb_reserva.id'))
    