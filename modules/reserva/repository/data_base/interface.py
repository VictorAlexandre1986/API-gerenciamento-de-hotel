from datetime import datetime
from abc import ABC, abstractmethod

class ReservaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_reserva(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_reservas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_reserva_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_reserva_por_mes(self, mes: datetime):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_reserva(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_reserva(self, id: int):
        raise Exception("Método não implementado")