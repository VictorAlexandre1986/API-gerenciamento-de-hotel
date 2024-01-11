from datetime import datetime

class ReservaUseCase:
    
    def __init__(self, reserva_repository):
        self.reserva_repository = reserva_repository
        
    
    def criar_reserva(self, id_cliente:int, qts_quartos: int, qts_dias:int, data_reserva: str, preco: float):
        return self.reserva_repository.criar_reserva(id, id_cliente, qts_quartos, qts_dias, data_reserva, preco)
    
    def buscar_reservas(self):
        return self.reserva_repository.buscar_reservas()

    def buscar_reservas_por_id(self, id: int):
        return self.reserva_repository.buscar_reservas_por_id(id)
    
    def buscar_reservas_por_mes(self, mes: str):
        #Converter mes para datetime
        return self.reserva_repository.buscar_reservas_por_mes(mes)
        
    def deletar_reserva(self, id: int):
        return self.reserva_repository.deletar_reserva(id)
    
    def atualizar_reserva(self, id:int,id_cliente:int, qts_quartos: int, qts_dias:int, data_reserva: str, preco: float):
        return self.salario_repository.atualizar_salario(id, id_cliente, qts_quartos, qts_dias, data_reserva, preco)