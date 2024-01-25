from modules.cliente_compra_produto.dto import ClienteCompraProdutoDTO
from modules.cliente_compra_produto.repository.data_base.cliente_compra_produto_repo import ClienteCompraProdutoRepository
from modules.cliente_compra_produto.usecase import ClienteCompraProdutoUseCase



class ProdutoController:

    @staticmethod
    def criar_produto(data: dict):
        data_dto = ClienteCompraProdutoDTO(**data)
        repository = ClienteCompraProdutoRepository()
        result = ClienteCompraProdutoUseCase(repository).criar_cliente_compra_produto(id = data_dto.id, id_cliente = data_dto.id_cliente, id_produto = data_dto.id_produto, qtd=data_dto.qtd)
        return result
    
    @staticmethod
    def buscar_cliente_compra_produto_por_id_cliente(id: int):
        repository = ClienteCompraProdutoRepository()
        result = ClienteCompraProdutoUseCase(repository).buscar_cliente_compra_produto_por_id_cliente(id)
        return result
    
    @staticmethod
    def buscar_clientes_compras_produtos():
        repository = ClienteCompraProdutoRepository()
        result = ClienteCompraProdutoUseCase(repository).buscar_clientes_compras_produtos()
        result = [compra.dict() for compra in result]
        return result
    
    @staticmethod
    def atualizar_produto(data: dict, id: int):
        data_dto = ClienteCompraProdutoDTO(**data)
        repository = ClienteCompraProdutoRepository()
        result = ClienteCompraProdutoUseCase(repository).atualizar_cliente_compra_produto(id=id, id_cliente = data_dto.id_cliente, id_produto = data_dto.id_produto, qtd = data_dto.qtd)
        return result
    
    @staticmethod
    def deletar_produto(id: int):
        repository = ClienteCompraProdutoRepository()
        result = ClienteCompraProdutoUseCase(repository).deletar_cliente_compra_produto(id)
        return result