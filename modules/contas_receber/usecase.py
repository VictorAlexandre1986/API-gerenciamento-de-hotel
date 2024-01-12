from datetime import datetime

class ContasReceberUseCase:
    
    def __init__(self, contas_receber_repository):
        self.contas_receber_repository = contas_receber_repository
        
    
    def criar_contas_receber(self, id_cliente:int,  valor: float, status:str, id_produto:int, id_reserva:int):
        return self.contas_receber_repository.criar_contas_receber(id, id_cliente,valor, status, id_produto, id_reserva)
    
    def buscar_contas_receber_por_mes(self, mes: str):
        # converter a string mes por datetime
        return self.contas_receber_repository.buscar_contas_receber_por_mes(mes)

    def buscar_contas_receber(self):
        return self.contas_receber_repository.buscar_contas_receber()
    
    def deletar_contas_receber(self, id: int):
        return self.contas_receber_repository.deletar_contas_receber(id)
    
    def atualizar_contas_receber(self, id:int, id_cliente: int,  valor:float, status:str, id_produto:int, id_reserva:int):
        return self.contas_pagar_repository.atualizar_contas_pagar(id, id_cliente,  valor, status, id_produto, id_reserva)