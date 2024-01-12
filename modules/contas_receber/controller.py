from modules.contas_receber.dto import ContasReceberDTO
from modules.contas_receber.repository.data_base.contas_receber_repo import ContasReceberRepository
from modules.contas_receber.usecase import ContasReceberUseCase



class ContasReceberController:

    @staticmethod
    def criar_contas_receber(data: dict):
        data_dto = ContasReceberDTO(**data)
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).criar_contas_receber(id = data_dto.id, id_cliente= data_dto.id_cliente, valor = data_dto.valor,  status=data_dto.status, id_produto=data_dto.id_produto, id_reserva=data_dto.id_reserva)
        return result
    
    @staticmethod
    def buscar_contas_receber_por_mes(mes: str):
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).buscar_contas_receber_por_mes(mes)
        return result
    
    
    @staticmethod
    def buscar_contas_receber():
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).buscar_contas_receber()
        result = [conta.dict() for conta in result]
        return result
    
    @staticmethod
    def atualizar_contas_receber(data: dict, id: int):
        data_dto = ContasReceberDTO(**data)
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).atualizar_contas_receber(id = id, id_cliente= data_dto.id_cliente, valor = data_dto.valor,   status=data_dto.status , id_produto=data_dto.id_produto, id_reserva=data_dto.id_reserva)
        return result
    
    @staticmethod
    def deletar_contas_receber(id: int):
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).deletar_contas_receber(id)
        return result