from modules.salario.dto import SalarioDTO
from modules.salario.repository.data_base.salario_repo import SalarioRepository
from modules.salario.usecase import SalarioUseCase



class SalarioController:

    @staticmethod
    def criar_salario(data: dict):
        data_dto = SalarioDTO(**data)
        repository = SalarioRepository()
        result = SalarioUseCase(repository).criar_salario(id = data_dto.id, id_funcionario = data_dto.id_funcionario, salario = data_dto.salario, salario_status= data_dto.salario_status, vale_refeicao=data_dto.vale_refeicao, vale_refeicao_status= data_dto.vale_refeicao_status, auxilio_medico=  data_dto.auxilio_medico, auxilio_medico_status=data_dto.auxilio_medico_status)
        return result
    
    @staticmethod
    def buscar_salario_por_status(pago: bool):
        repository = SalarioRepository()
        result = SalarioUseCase(repository).buscar_salarios_por_status(pago)
        return result

    @staticmethod
    def buscar_vale_refeicao_por_status(vale_refeicao: bool):
        repository = SalarioRepository()
        result = SalarioUseCase(repository).buscar_vale_refeicao_por_status(vale_refeicao)
        return result
    
    @staticmethod
    def buscar_auxilio_medico_por_status(auxilio_medico: bool):
        repository = SalarioRepository()
        result = SalarioUseCase(repository).buscar_auxilio_medico_por_status(auxilio_medico)
        return result
    
    @staticmethod
    def buscar_salarios():
        repository = SalarioRepository()
        result = SalarioUseCase(repository).buscar_salarios()
        result = [salario.dict() for salario in result]
        return result
    
    @staticmethod
    def atualizar_salario(data: dict, id: int):
        data_dto = SalarioDTO(**data)
        repository = SalarioRepository()
        result = SalarioUseCase(repository).atualizar_salario(id=id, id_funcionario = data_dto.id_funcionario, salario = data_dto.salario, salario_status= data_dto.salario_status, vale_refeicao=data_dto.vale_refeicao, vale_refeicao_status= data_dto.vale_refeicao_status, auxilio_medico=  data_dto.auxilio_medico, auxilio_medico_status=data_dto.auxilio_medico_status)
        return result
    
    @staticmethod
    def deletar_salario(id: int):
        repository = SalarioRepository()
        result = SalarioUseCase(repository).deletar_salario(id)
        return result