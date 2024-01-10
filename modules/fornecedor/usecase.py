from datetime import datetime

class ContasPagarUseCase:
    
    def __init__(self, fornecedor_repository):
        self.fornecedor_repository = fornecedor_repository
        
    
    def criar_fornecedor(self, fornecedor:str, cnpj: str, contato: str):
        return self.fornecedor_repository.criar_fornecedor(id,fornecedor, cnpj,contato)

    def buscar_contas_pagar_por_fornecedor(self, fornecedor: str):
        return self.fornecedor_repository.buscar_por_fornecedor(fornecedor)
    
    def buscar_por_fornecedores(self):
        return self.fornecedor_repository.buscar_fornecedor()
    
    def deletar_fornecedor(self, id: int):
        return self.fornecedor_repository.deletar_fornecedor(id)
    
    def atualizar_fornecedor(self, id:int, fornecedor: str, cnpj:str, contato:str):
        return self.fornecedor_repository.atualizar_fornecedor(id, fornecedor, cnpj, contato)