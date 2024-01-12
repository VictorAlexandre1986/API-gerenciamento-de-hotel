from datetime import datetime

class FuncionarioUseCase:
    
    def __init__(self, funcionario_repository):
        self.funcionario_repository = funcionario_repository
        
    
    def criar_funcionario(self, nome:str, cpf: str,  endereco: str, bairro:str, cidade:str, contato:str, data_nascimento:str, id_cargo:int):
        # converter a dt_nasc para datetime
        return self.funcionario_repository.criar_funcionario(id, nome, cpf,endereco, bairro,cidade,contato,data_nascimento, id_cargo)
    
    def buscar_funcionarios(self):
        return self.funcionario_repository.buscar_funcionarios()
    
    def buscar_funcionario_por_nome(self, nome:str):
        return self.funcionario_repository.buscar_funcionario_por_nome(nome)
    
    def deletar_funcionario(self, id: int):
        return self.funcionario_repository.deletar_funcionario(id)
    
    def atualizar_funcionario(self, id:int, nome: str, cpf:str, endereco:str, bairro:str, cidade:str, contato:str, data_nascimento:str, id_cargo:int):
        return self.funcionario_repository.atualizar_funcionario(id, nome, cpf, endereco, bairro, cidade, contato, data_nascimento,id_cargo)