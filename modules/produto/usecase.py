from datetime import datetime

class ProdutoUseCase:
    
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository
        
    
    def criar_produto(self, nome:str, categoria: int,  valor_custo: float, valor_venda:float, id_fornecedor:int, data_validade:str):
        # converter a dt_nasc para datetime
        return self.produto_repository.criar_produto(id, nome, categoria,valor_custo, valor_venda,id_fornecedor,data_validade)
    
    def buscar_produtos(self):
        return self.produto_repository.buscar_produtos()
    
    def buscar_produto_por_nome(self, nome:str):
        return self.produto_repository.buscar_produto_por_nome(nome)
    
    def deletar_produto(self, id: int):
        return self.produto_repository.deletar_produto(id)
    
    def atualizar_produto(self, id:int, nome:str, categoria: int,  valor_custo: float, valor_venda:float, id_fornecedor:int, data_validade:str):
        return self.produto_repository.atualizar_produto(id, nome, categoria,valor_custo, valor_venda,id_fornecedor,data_validade)