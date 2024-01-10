from abc import ABC, abstractmethod
from datetime import datetime

class FornecedorRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_fornecedor(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_fornecedores(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_fornecedores_por_nome(self, nome:str):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_fornecedor(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_fornecedor(self, id: int):
        raise Exception("Método não implementado")