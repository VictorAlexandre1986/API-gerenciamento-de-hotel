from datetime import datetime

class ClienteCompraProdutoUseCase:
    
    def __init__(self, cliete_compra_produto_repository):
        self.cliete_compra_produto_repository = cliete_compra_produto_repository
        
    
    def criar_compra_produto(self, id_cliente:int,  id_produto, qtd: int):
        return self.cliente_compra_produto_repository.criar_cliente_compra_produto(id, id_cliente,id_produto,qtd)
    
    def buscar_cliente_compra_produto_por_id_cliente(self, id_cliente: int):
        return self.cliente_compra_produto_repository.buscar_cliente_compra_produto_por_id_cliente(id_cliente)

    def buscar_clientes_compras_produtos(self):
        return self.cliente_compra_produto_repository.buscar_clientes_compras_produtos()
    
    def deletar_cliente_compra_produto(self, id: int):
        return self.cliente_compra_produto_repository.deletar_cliente_compra_produto(id)
    
    def atualizar_cliente_compra_produto(self, id:int, id_cliente: int,  id_produto:int, qtd: int):
        return self.cliente_compra_produto_repository.atualizar_cliente_compra_produto(id, id_cliente, id_produto, qtd)