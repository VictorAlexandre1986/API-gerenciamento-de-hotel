from datetime import datetime

class SalarioUseCase:
    
    def __init__(self, salario_repository):
        self.salario_repository = salario_repository
        
    
    def criar_salario(self, id_funcionario:int, salario: float, salario_status:bool, vale_refeicao: float, vale_refeicao_status:bool, auxilio_medico:float, auxilio_medico_status:bool):
        return self.salario_repository.criar_salario(id, id_funcionario, salario,salario_status, vale_refeicao,vale_refeicao_status,auxilio_medico,auxilio_medico_status)
    
    def buscar_salarios(self):
        return self.salario_repository.buscar_salarios()
    
    def buscar_salarios_por_status(self, salario_status:bool):
        return self.salario_repository.buscar_salario_por_status(salario_status)
    
    def buscar_vale_refeicao_por_status(self, vale_refeicao_status:bool):
        return self.salario_repository.buscar_vale_refeicao_por_status(vale_refeicao_status)
    
    def buscar_auxilio_medico_por_status(self, auxilio_medico_status:bool):
        return self.salario_repository.buscar_auxilio_medico_por_status(auxilio_medico_status)
    
    def deletar_salario(self, id: int):
        return self.salario_repository.deletar_salario(id)
    
    def atualizar_salario(self, id:int,id_funcionario:int, salario: float, salario_status:bool, vale_refeicao: float, vale_refeicao_status:bool, auxilio_medico:float, auxilio_medico_status:bool):
        return self.salario_repository.atualizar_salario(id, id_funcionario, salario,salario_status, vale_refeicao,vale_refeicao_status,auxilio_medico,auxilio_medico_status)