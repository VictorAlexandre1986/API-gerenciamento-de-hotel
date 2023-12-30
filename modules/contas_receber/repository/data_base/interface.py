from abc import ABC, abstractmethod
from datetime import datetime

class ContasReceberRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_contas_receber(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_contas_receber(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_contas_receber_por_mes(self, mes: datetime):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_contas_receber(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_contas_receber(self, id: int):
        raise Exception("Método não implementado")