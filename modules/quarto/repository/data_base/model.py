from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from modules.reserva.repository.data_base.model import Reserva

from infra.db import Base

class Quarto(Base):
    __tablename__ = "tb_quarto"
    
    tipo = Column(String, nullable=False)
    preco_aluguel = Column(Float, nullable=False)
    alugado = Column(Boolean, nullable=False)
    reserva = relationship(Reserva, back_populates='quarto')