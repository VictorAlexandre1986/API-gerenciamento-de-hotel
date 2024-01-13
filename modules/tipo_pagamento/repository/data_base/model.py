from sqlalchemy import Column, Float, String, DateTime, Integer, ForeignKey
from modules.salario.repository.data_base.model import Salario
from modules.contas_pagar.repository.data_base.model import ContasPagar
from modules.contas_receber.repository.data_base.model import ContasReceber
from sqlalchemy.orm import relationship

from infra.db import Base

class TipoPagamento(Base):
    __tablename__ = "tb_tipo_pagamento"
    
    tipo_pagamento = Column(String, nullable=False)
    salario = relationship(Salario, back_populates='tb_tipo_pagamento')
    contas_pagar = relationship(ContasPagar, back_populates='tb_tipo_pagamento')
    contas_receber = relationship(ContasReceber, back_populates='tb_tipo_pagamento')
   
    