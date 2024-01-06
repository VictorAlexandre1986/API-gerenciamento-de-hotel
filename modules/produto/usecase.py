from datetime import datetime

class ProdutoUseCase:
    
    def __init__(self, produto_repository):
        self.produto_repository = produto_repository
        
    
    def criar_produto(self, nome:str, categoria: int,  valor_custo: float, valor_venda:float, fornecedor:str, data_validade:str):
        # converter a dt_nasc para datetime
        return self.funcionario_repository.criar_funcionario(id, nome, categoria,valor_custo, valor_venda,fornecedor,data_validade)
    
    def buscar_funcionario(self):
        return self.funcionario_repository.buscar_funcionario()
    
    def buscar_funcionario_por_nome(self, nome:str):
        return self.funcionario_repository.buscar_funcionario_por_nome(nome)
    
    def deletar_funcionario(self, id: int):
        return self.funcionario_repository.deletar_funcionario(id)
    
    def atualizar_funcionario(self, id:int, nome:str, categoria: int,  valor_custo: float, valor_venda:float, fornecedor:str, data_validade:str):
        return self.funcionario_repository.atualizar_funcionario(id, nome, categoria,valor_custo, valor_venda,fornecedor,data_validade)