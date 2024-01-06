from abc import ABC, abstractmethod
from datetime import datetime

class FuncionarioRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_funcionario(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_funcionarios(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_funcionario_por_nome(self, nome: str):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_funcionario(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_funcionario(self, id: int):
        raise Exception("Método não implementado")