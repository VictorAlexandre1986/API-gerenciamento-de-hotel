from sqlalchemy import Column, Integer, Float,Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from modules.cliente.repository.data_base.model import Cliente


from infra.db import Base

class Reserva(Base):
    __tablename__ = "tb_reserva"
    
    num_quarto = Column(Integer, nullable=False)
    qts_dias = Column(Integer, nullable=False)
    data_reserva = Column(DateTime, nullable=False)
    preco = Column(Float, nullable=False)
    id_cliente = Column(Integer, ForeignKey('tb_cliente.id'))
    id_quarto = Column(Integer, ForeignKey('tb_quato.id'))