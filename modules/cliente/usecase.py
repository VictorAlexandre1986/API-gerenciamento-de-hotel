from datetime import datetime

class ClienteUseCase:
    
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository
        
    
    def criar_cliente(self, nome: str,cpf:str, dt_nasc:str,sexo:str,endereco:str,bairro:str,cidade:str,estado:str,contato:str):
        return self.cliente_repository.criar_cliente(id, nome,cpf,dt_nasc,sexo,endereco,bairro,cidade,estado,contato)
    
    def buscar_clientes(self):
        return self.cliente_repository.buscar_clientes()
    
    def buscar_cliente_por_cpf(self, cpf:str):
        return self.cliente_repository.buscar_cliente_por_cpf(cpf)
    
    def deletar_cliente(self, id: int):
        return self.cliente_repository.deletar_cliente(id)
    
    def atualizar_cliente(self, id:int ,nome: str,cpf:str, dt_nasc:str,sexo:str,endereco:str,bairro:str,cidade:str,estado:str,contato:str):
        return self.cliente_repository.atualizar_cliente(id, nome,cpf,dt_nasc,sexo,endereco,bairro,cidade,estado,contato)