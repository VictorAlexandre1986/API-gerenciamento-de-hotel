from sqlalchemy import Column, Float, String, DateTime, Integer, ForeignKey
from modules.cliente_compra_produto.repository.data_base.model import ClienteCompraProduto
from sqlalchemy.orm import relationship

from infra.db import Base

class ClienteCompraProduto(Base):
    __tablename__ = "tb_cliente_compra_produto"
    
    id_cliente = Column(String, ForeignKey('tb_cliente'))
    id_produto = Column(Integer, ForeignKey('tb_funcionario.id'))
    qtd = Column(Integer, nullable=False)
