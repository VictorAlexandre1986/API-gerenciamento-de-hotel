from abc import ABC, abstractmethod

class ProdutoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_produto(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_produtos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_produto_por_nome(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_produto(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_produto(self, id: int):
        raise Exception("Método não implementado")