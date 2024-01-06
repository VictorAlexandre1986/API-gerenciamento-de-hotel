from sqlalchemy import Column, Integer, Float,Boolean, ForeignKey
from sqlalchemy.orm import relationship
from modules.funcionario.repository.data_base.model import Funcionario


from infra.db import Base

class Salario(Base):
    __tablename__ = "tb_salario"
    
    salario = Column(Float, nullable=False)
    salario_status = Column(Boolean, nullable=False)
    vale_refeicao = Column(Float, nullable=False)
    vale_refeicao_status = Column(Boolean, nullable=False)
    auxilio_medico = Column(Float, nullable=False)
    auxilio_medico_status = Column(Boolean, nullable=False)
    id_funcionario = Column(Integer, ForeignKey('tb_funcionario.id'))
    funcionario = relationship(Funcionario, back_populates='tb_salario')