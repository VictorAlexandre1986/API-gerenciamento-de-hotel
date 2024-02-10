from abc import ABC, abstractmethod

class QuartoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_quarto(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_quartos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_quarto_por_tipo(self, tipo: str):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_quarto_por_preco_aluguel(self, preco_aluguel: float):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_quarto_por_alugado(self, alugado: bool):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_quarto(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_quarto(self, id: int):
        raise Exception("Método não implementado")