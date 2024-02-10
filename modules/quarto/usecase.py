from datetime import datetime

class QuartoUseCase:
    
    def __init__(self, quarto_repository):
        self.quarto_repository = quarto_repository
        
    
    def criar_quarto(self, tipo:str, preco_aluguel: float,  alugado: bool):
        return self.quarto_repository.criar_quarto(id, tipo, preco_aluguel,alugado)
    
    def buscar_quartos(self):
        return self.quarto_repository.buscar_quartos()
    
    def buscar_quarto_por_tipo(self, tipo:str):
        return self.quarto_repository.buscar_quarto_por_tipo(tipo)
    
    def buscar_quarto_por_alugado(self, alugado:bool):
        return self.quarto_repository.buscar_quarto_por_alugado(alugado)
    
    def buscar_quarto_por_preco(self, preco: float):
        return self.quarto_repository.buscar_quarto_por_preco(preco)
    
    def deletar_quarto(self, id: int):
        return self.quarto_repository.deletar_quarto(id)
    
    def atualizar_quarto(self, id:int, tipo:str, preco_aluguel: float,  alugado: bool):
        return self.quarto_repository.atualizar_quarto(id, tipo, preco_aluguel,alugado)