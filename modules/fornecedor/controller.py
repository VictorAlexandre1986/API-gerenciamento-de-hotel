from modules.fornecedor.dto import FornecedorDTO
from modules.fornecedor.repository.data_base.contas_pagar_repo import FornecedorRepository
from modules.fornecedor.usecase import FornecedorUseCase



class FornecedorController:

    @staticmethod
    def criar_fornecedor(data: dict):
        data_dto = FornecedorDTO(**data)
        repository = FornecedorRepository()
        result = FornecedorUseCase(repository).criar_fornecedor(id = data_dto.id, fornecedor= data_dto.fornecedor, cnpj = data_dto.cnpj, contato = data_dto.contato)
        return result
    
    
    @staticmethod
    def buscar_fornecedor(fornecedor: str):
        repository = FornecedorRepository()
        result = FornecedorUseCase(repository).buscar_fornecedor(fornecedor)
        return result
    
    @staticmethod
    def buscar_fornecedores():
        repository = FornecedorRepository()
        result = FornecedorUseCase(repository).buscar_fornecedores()
        result = [conta.dict() for conta in result]
        return result
    
    @staticmethod
    def atualizar_fornecedor(data: dict, id: int):
        data_dto = FornecedorDTO(**data)
        repository = FornecedorRepository()
        result = FornecedorUseCase(repository).atualizar_fornecedor(id = id, fornecedor= data_dto.fornecedor, cnpj = data_dto.cnpj, contato = data_dto.contato)
        return result
    
    @staticmethod
    def deletar_fornecedor(id: int):
        repository = FornecedorRepository()
        result = FornecedorUseCase(repository).deletar_fornecedor(id)
        return result