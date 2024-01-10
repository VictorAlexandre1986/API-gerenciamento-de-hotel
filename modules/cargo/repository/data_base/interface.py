from abc import ABC, abstractmethod
from datetime import datetime

class CargoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_cargo(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_cargos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_cargo_por_nome(self, nome: str):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_cargo(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_cargo(self, id: int):
        raise Exception("Método não implementado")