from sqlalchemy import Column, Float, String, DateTime
from sqlalchemy.orm import relationship

from infra.db import Base

class ContasReceber(Base):
    __tablename__ = "tb_contas_receber"
    
    cliente = Column(String, nullable=False)
    vencimento = Column(DateTime, nullable=False)
    valor = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    