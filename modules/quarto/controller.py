from modules.quarto.dto import QuartoDTO
from modules.quarto.repository.data_base.quarto_repo import QuartoRepository
from modules.quarto.usecase import QuartoUseCase



class QuartoController:

    @staticmethod
    def criar_quarto(data: dict):
        data_dto = QuartoDTO(**data)
        repository = QuartoRepository()
        result = QuartoUseCase(repository).criar_quarto(id = data_dto.id, tipo = data_dto.tipo, preco_aluguel = data_dto.preco_aluguel, alugado = data_dto.alugado)
        return result
    
    @staticmethod
    def buscar_quarto_por_tipo(nome: str):
        repository = QuartoRepository()
        result = QuartoUseCase(repository).buscar_quarto_por_tipo(nome)
        return result
    
    @staticmethod
    def buscar_quarto_por_preco(preco: float):
        repository = QuartoRepository()
        result = QuartoUseCase(repository).buscar_quarto_por_preco(preco)
        return result
    
    @staticmethod
    def buscar_quarto_por_alugado(alugado: bool):
        repository = QuartoRepository()
        result = QuartoUseCase(repository).buscar_quarto_por_alugado(alugado)
        return result
    
    @staticmethod
    def buscar_quartos():
        repository = QuartoRepository()
        result = QuartoUseCase(repository).buscar_quartos()
        result = [quarto.dict() for quarto in result]
        return result
    
    @staticmethod
    def atualizar_quarto(data: dict, id: int):
        data_dto = QuartoDTO(**data)
        repository = QuartoRepository()
        result = QuartoUseCase(repository).atualizar_quarto(id=id, tipo = data_dto.tipo, preco_aluguel = data_dto.preco_aluguel, alugado= data_dto.alugado)
        return result
    
    @staticmethod
    def deletar_quarto(id: int):
        repository = QuartoRepository()
        result = QuartoUseCase(repository).deletar_quarto(id)
        return result