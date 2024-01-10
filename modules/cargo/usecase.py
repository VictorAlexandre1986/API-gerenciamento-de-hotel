from datetime import datetime

class CargoUseCase:
    
    def __init__(self, cargo_repository):
        self.cargo_repository = cargo_repository
        
    
    def criar_cargo(self, cargo: str):
        return self.cargo_repository.criar_cargo(id, cargo)
    
    def buscar_cargos(self):
        return self.cargo_repository.buscar_cargos()
    
    def buscar_cargo_por_id(self, id:int):
        return self.cargo_repository.buscar_cargo_por_id(id)
    
    def deletar_cargo(self, id: int):
        return self.cargo_repository.deletar_cargo(id)
    
    def atualizar_cargo(self, id:int ,cargo:str):
        return self.cargo_repository.atualizar_cargo(id, cargo)