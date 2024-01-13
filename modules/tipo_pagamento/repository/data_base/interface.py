from datetime import datetime
from abc import ABC, abstractmethod

class TipoPagamentoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_tipo_pagamento(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_tipos_pagamentos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_tipo_pagamento_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_tipo_pagamento(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_tipo_pagamento(self, id: int):
        raise Exception("Método não implementado")