from abc import ABC, abstractmethod

class SalarioRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_salario(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_salarios(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_salario_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_salario(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_salario(self, id: int):
        raise Exception("Método não implementado")