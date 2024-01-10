from modules.cargo.dto import CargoDTO
from modules.cargo.repository.data_base.cargo_repo import CargoRepository
from modules.cargo.usecase import CargoUseCase



class CargoController:

    @staticmethod
    def criar_cargo(data: dict):
        data_dto = CargoDTO(**data)
        repository = CargoRepository()
        result = CargoUseCase(repository).criar_cargo(id = data_dto.id, cargo = data_dto.cargo)
        return result
    
    @staticmethod
    def buscar_cargo_por_nome(nome: str):
        repository = CargoRepository()
        result = CargoUseCase(repository).buscar_cargo_por_nome(nome)
        return result
    
    
    @staticmethod
    def buscar_cargos():
        repository = CargoRepository()
        result = CargoUseCase(repository).buscar_cargos()
        result = [cargo.dict() for cargo in result]
        return result
    
    @staticmethod
    def atualizar_cargo(data: dict, id: int):
        data_dto = CargoDTO(**data)
        repository = CargoRepository()
        result = CargoUseCase(repository).atualizar_cargo(id = id, cargo = data_dto.cargo)
        return result
    
    @staticmethod
    def deletar_cargo(id: int):
        repository = CargoRepository()
        result = CargoUseCase(repository).deletar_cargo(id)
        return result