from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship

from infra.db import Base

class ContasPagar(Base):
    __tablename__ = "tb_contas_pagar"
    
    
    fornecedor = Column(String)
    servico = Column(String)
    produto = Column(String)
    valor = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    