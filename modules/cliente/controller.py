from modules.cliente.dto import ClienteDTO
from modules.cliente.repository.data_base.cliente_repo import ClienteRepository
from modules.cliente.usecase import ClienteUseCase



class ClienteController:

    @staticmethod
    def criar_cliente(data: dict):
        data_dto = ClienteDTO(**data)
        repository = ClienteRepository()
        result = ClienteUseCase(repository).criar_cliente(id = data_dto.id, nome = data_dto.nome, cpf= data_dto.cpf, dt_nasc=data_dto.dt_nasc, sexo = data_dto.sexo,endereco=data_dto.endereco, bairro=data_dto.bairro, cidade= data_dto.cidade,estado=data_dto.estado, contato=data_dto.contato)
        return result
    
    @staticmethod
    def buscar_cliente_por_cpf(cpf: str):
        repository = ClienteRepository()
        result = ClienteUseCase(repository).buscar_cliente_por_cpf(cpf)
        return result
    
    
    @staticmethod
    def buscar_clientes():
        repository = ClienteRepository()
        result = ClienteUseCase(repository).buscar_clientes()
        result = [cargo.dict() for cargo in result]
        return result
    
    @staticmethod
    def atualizar_cliente(data: dict, id: int):
        data_dto = ClienteDTO(**data)
        repository = ClienteRepository()
        result = ClienteUseCase(repository).atualizar_cliente(id = id, nome = data_dto.nome, cpf= data_dto.cpf, dt_nasc=data_dto.dt_nasc, sexo = data_dto.sexo,endereco=data_dto.endereco, bairro=data_dto.bairro, cidade= data_dto.cidade,estado=data_dto.estado, contato=data_dto.contato)
        return result
    
    @staticmethod
    def deletar_cliente(id: int):
        repository = ClienteRepository()
        result = ClienteUseCase(repository).deletar_cliente(id)
        return result