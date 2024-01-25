from modules.reserva.dto import ReservaDTO
from modules.reserva.repository.data_base.reserva_repo import ReservaRepository
from modules.reserva.usecase import ReservaUseCase



class ReservaController:

    @staticmethod
    def criar_reserva(data: dict):
        data_dto = ReservaDTO(**data)
        repository = ReservaRepository()
        result = ReservaUseCase(repository).criar_reserva(id = data_dto.id, id_cliente = data_dto.id_cliente, id_quarto= data_dto.id_quarto, qts_dias= data_dto.qts_dias, preco=data_dto.preco, data_reserva = data_dto.data_reserva)
        return result
    
    @staticmethod
    def buscar_reserva_por_id(id: int):
        repository = ReservaRepository()
        result = ReservaUseCase(repository).buscar_reserva_por_id(id)
        return result
    
    @staticmethod
    def buscar_reserva_por_data(data: str):
        repository = ReservaRepository()
        result = ReservaUseCase(repository).buscar_reserva_por_data(data)
        result = [reserva.dict() for reserva in result]
        return result

    @staticmethod
    def buscar_reserva_disponivel(disponivel: bool):
        repository = ReservaRepository()
        result = ReservaUseCase(repository).buscar_reserva_disponivel(disponivel)
        result = [reserva.dict() for reserva in result]
        return result
    
    @staticmethod
    def buscar_reservas():
        repository = ReservaRepository()
        result = ReservaUseCase(repository).buscar_reservas()
        result = [reserva.dict() for reserva in result]
        return result
    
    @staticmethod
    def atualizar_reserva(data: dict, id: int):
        data_dto = ReservaDTO(**data)
        repository = ReservaRepository()
        result = ReservaUseCase(repository).atualizar_reserva(id=id, id_cliente = data_dto.id_cliente, id_quarto=  data_dto.id_quarto, qts_dias= data_dto.qts_dias, preco=data_dto.preco, data_reserva= data_dto.data_reserva)
        return result
    
    @staticmethod
    def deletar_reserva(id: int):
        repository = ReservaRepository()
        result = ReservaUseCase(repository).deletar_reserva(id)
        return result