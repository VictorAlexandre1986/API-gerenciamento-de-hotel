from abc import ABC, abstractmethod
from datetime import datetime

class ClienteCompraProdutoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_cliente_compra_produto(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_clientes_compras_produtos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_cliente_compra_produto_por_id_cliente(self, id: int):
        raise Exception("Método não implementado")

    @abstractmethod
    def atualizar_cliente_compra_produto(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_cliente_compra_produto(self, id: int):
        raise Exception("Método não implementado")