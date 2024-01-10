from abc import ABC, abstractmethod
from datetime import datetime

class ContasPagarRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_contas_pagar(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_contas_pagar(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_contas_pagar_por_mes(self, mes: datetime):
        raise Exception("Método não implementado")

    @abstractmethod
    def buscar_contas_pagar_por_fornecedor(self, fornecedor: str):
        raise Exception("Método não implementado")

    @abstractmethod
    def buscar_contas_pagar_por_servico(self, servico: str):
        raise Exception("Método não implementado")

    @abstractmethod
    def buscar_contas_pagar_por_produto(self, produto: id):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_contas_pagar(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_contas_pagar(self, id: int):
        raise Exception("Método não implementado")