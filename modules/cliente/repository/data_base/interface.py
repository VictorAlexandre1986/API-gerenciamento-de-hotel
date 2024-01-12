from abc import ABC, abstractmethod
from datetime import datetime

class ClienteRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_cliente(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_clientes(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_cliente_por_cpf(self, nome: str):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_cliente(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_cliente(self, id: int):
        raise Exception("Método não implementado")