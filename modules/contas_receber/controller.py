from modules.contas_receber.dto import ContasReceberDTO
from modules.contas_receber.repository.data_base.contas_receber_repo import ContasReceberRepository
from modules.contas_receber.usecase import ContasReceberUseCase



class ContasReceberController:

    @staticmethod
    def criar_contas_receber(data: dict):
        data_dto = ContasReceberDTO(**data)
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).criar_contas_receber(id = data_dto.id, cliente= data_dto.cliente, valor = data_dto.valor, vencimento = data_dto.vencimento,  status=data_dto.status)
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
        result = [login.dict() for login in result]
        return result
    
    @staticmethod
    def atualizar_contas_receber(data: dict, id: int):
        data_dto = ContasReceberDTO(**data)
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).atualizar_contas_receber(id = id, cliente= data_dto.cliente, valor = data_dto.valor, vencimento = data_dto.vencimento,  status=data_dto.status)
        return result
    
    @staticmethod
    def deletar_contas_receber(id: int):
        repository = ContasReceberRepository()
        result = ContasReceberUseCase(repository).deletar_contas_receber(id)
        return result