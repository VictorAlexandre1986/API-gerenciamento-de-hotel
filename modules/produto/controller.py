from modules.produto.dto import ProdutoDTO
from modules.produto.repository.data_base.produto_repo import ProdutoRepository
from modules.produto.usecase import ProdutoUseCase



class ProdutoController:

    @staticmethod
    def criar_produto(data: dict):
        data_dto = ProdutoDTO(**data)
        repository = ProdutoRepository()
        result = ProdutoUseCase(repository).criar_produto(id = data_dto.id, nome = data_dto.nome, categoria = data_dto.categoria, preco_custo = data_dto.preco_custo, preco_venda= data_dto.preco_venda, id_fornecedor= data_dto.id_fornecedor, data_validade = data_dto.data_validade)
        return result
    
    @staticmethod
    def buscar_produto_por_id(id: int):
        repository = ProdutoRepository()
        result = ProdutoUseCase(repository).buscar_produto_por_id(id)
        return result
    
    @staticmethod
    def buscar_produtos():
        repository = ProdutoRepository()
        result = ProdutoUseCase(repository).buscar_produtos()
        result = [produto.dict() for produto in result]
        return result
    
    @staticmethod
    def atualizar_produto(data: dict, id: int):
        data_dto = ProdutoDTO(**data)
        repository = ProdutoRepository()
        result = ProdutoUseCase(repository).atualizar_produto(id=id, nome = data_dto.nome, categoria = data_dto.categoria, preco_custo = data_dto.preco_custo, preco_venda= data_dto.preco_venda, id_fornecedor= data_dto.id_fornecedor, data_validade = data_dto.data_validade)
        return result
    
    @staticmethod
    def deletar_produto(id: int):
        repository = ProdutoRepository()
        result = ProdutoUseCase(repository).deletar_produto(id)
        return result