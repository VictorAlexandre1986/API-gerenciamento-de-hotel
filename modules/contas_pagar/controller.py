from modules.contas_pagar.dto import ContasPagarDTO
from modules.contas_pagar.repository.data_base.contas_pagar_repo import ContasPagarRepository
from modules.contas_pagar.usecase import ContasPagarUseCase



class ContasPagarController:

    @staticmethod
    def criar_contas_pagar(data: dict):
        data_dto = ContasPagarDTO(**data)
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).criar_contas_pagar(id = data_dto.id, fornecedor= data_dto.fornecedor, servico = data_dto.servico, id_produto = data_dto.id_produto, valor = data_dto.valor, status=data_dto.status, data = data_dto.data)
        return result
    
    @staticmethod
    def buscar_contas_pagar_por_mes(mes: str):
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).buscar_contas_pagar_por_mes(mes)
        return result
    
    @staticmethod
    def buscar_contas_pagar_por_fornecedor(fornecedor: str):
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).buscar_contas_pagar_por_fornecedor(fornecedor)
        return result
    
    @staticmethod
    def buscar_contas_pagar_por_servico(servico: str):
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).buscar_contas_pagar_por_servico(servico)
        return result
    
    @staticmethod
    def buscar_contas_pagar():
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).buscar_contas_pagar()
        result = [conta.dict() for conta in result]
        return result
    
    @staticmethod
    def atualizar_contas_pagar(data: dict, id: int):
        data_dto = ContasPagarDTO(**data)
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).atualizar_contas_pagar(id = id, fornecedor= data_dto.fornecedor, servico = data_dto.servico, produto = data_dto.produto, valor = data_dto.valor, status= data_dto.status, data= data_dto.data)
        return result
    
    @staticmethod
    def deletar_contas_pagar(id: int):
        repository = ContasPagarRepository()
        result = ContasPagarUseCase(repository).deletar_contas_pagar(id)
        return result