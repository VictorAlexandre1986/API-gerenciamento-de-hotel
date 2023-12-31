from modules.funcionario.dto import FuncionarioDTO
from modules.funcionario.repository.data_base.contas_receber_repo import FuncionarioRepository
from modules.funcionario.usecase import FuncionarioUseCase



class FuncionarioController:

    @staticmethod
    def criar_funcionario(data: dict):
        data_dto = FuncionarioDTO(**data)
        repository = FuncionarioRepository()
        result = FuncionarioUseCase(repository).criar_funcionario(id = data_dto.id, nome= data_dto.nome, cpf = data_dto.cpf, endereco = data_dto.endereco,  bairro=data_dto.bairro, cidade=data_dto.cidade,contato=data_dto.contato, data_nascimento=data_dto.data_nascimento)
        return result
    
    @staticmethod
    def buscar_funcionario_por_nome(nome: str):
        repository = FuncionarioRepository()
        result = FuncionarioUseCase(repository).buscar_funcionario_por_nome(nome)
        return result
    
    
    @staticmethod
    def buscar_funcionarios():
        repository = FuncionarioRepository()
        result = FuncionarioUseCase(repository).buscar_funcionarios()
        result = [funcionario.dict() for funcionario in result]
        return result
    
    @staticmethod
    def atualizar_fuuncionario(data: dict, id: int):
        data_dto = FuncionarioDTO(**data)
        repository = FuncionarioRepository()
        result = FuncionarioUseCase(repository).atualizar_funcionario(id = id,  nome= data_dto.nome, cpf = data_dto.cpf, endereco = data_dto.endereco,  bairro=data_dto.bairro, cidade=data_dto.cidade,contato=data_dto.contato, data_nascimento=data_dto.data_nascimento)
        return result
    
    @staticmethod
    def deletar_funcionario(id: int):
        repository = FuncionarioRepository()
        result = FuncionarioUseCase(repository).deletar_funcionario(id)
        return result