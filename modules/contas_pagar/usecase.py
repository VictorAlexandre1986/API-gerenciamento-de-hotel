from datetime import datetime

class ContasPagarUseCase:
    
    def __init__(self, contas_pagar_repository):
        self.contas_pagar_repository = contas_pagar_repository
        
    
    def criar_contas_pagar(self, fornecedor:str, servico: str, produto: str, valor: float, status:str):
        return self.contas_pagar_repository.criar_contas_pagar(id,fornecedor, servico,produto,valor, status)
    
    def buscar_contas_pagar_por_mes(self, mes: str):
        # converter a string mes por datetime
        return self.contas_pagar_repository.buscar_contas_pagar_por_mes(mes)

    def buscar_contas_pagar_por_fornecedor(self, fornecedor: str):
        return self.contas_pagar_repository.buscar_contas_pagar_por_fornecedor(fornecedor)
    
    def buscar_contas_pagar_por_servico(self, servico: str):
        return self.contas_pagar_repository.buscar_login_por_servico(servico)
    
    def buscar_contas_pagar(self):
        return self.contas_pagar_repository.buscar_contas_pagar()
    
    def deletar_contas_pagar(self, id: int):
        return self.contas_pagar_repository.deletar_contas_pagar(id)
    
    def atualizar_contas_pagar(self, id:int, fornecedor: str, servico:str, produto:str, valor:float, status:str):
        return self.contas_pagar_repository.atualizar_contas_pagar(id, fornecedor, servico, produto, valor, status)