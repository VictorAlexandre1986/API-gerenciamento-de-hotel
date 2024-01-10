from infra.db.db_config import DBConnectionHandler
from modules.funcionario.repository.data_base.interface import FuncionarioRepositoryInterface
from modules.funcionario.repository.data_base.model import Funcionario
from modules.funcionario.entity import FuncionarioEntity
from datetime import datetime
import uuid as uuid


class FuncionarioRepository(FuncionarioRepositoryInterface):

    def _criar_funcionario_objeto(self, funcionario):
        return FuncionarioEntity(
            id=funcionario.id,
            nome=funcionario.nome,
            cpf=funcionario.cpf,
            endereco= funcionario.endereco,
            bairro = funcionario.bairro,
            cidade = funcionario.cidade,
            contato = funcionario.contato,
            data_nascimento=funcionario.data_nascimento,
            id_cargo = funcionario.id_cargo
        )

    def criar_funcionario(self, id: int, nome: str, cpf:str, endereco:str, bairro:str, cidade:str, contato:str, data_nascimento:datetime, id_cargo: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_funcionario = Funcionario(id=id, nome=nome, cpf=cpf, endereco=endereco, bairro=bairro, cidade=cidade, contato=contato, data_nascimento=data_nascimento, id_cargo=id_cargo)
                db_connection.session.add(novo_funcionario)
                db_connection.session.commit()
                return self._criar_funcionario_objeto(novo_funcionario)
        except Exception as exc:
            raise exc

    def buscar_funcionario_por_nome(self, nome:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Funcionario).filter(Funcionario.nome == nome).one_or_none()
            data_resultado = self._criar_funcionario_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_funcionario(self):
        with DBConnectionHandler() as db_connection:
            list_funcionarios = []
            funcionarios = db_connection.session.query(Funcionario).all()
            for funcionario in funcionarios:
                list_funcionarios.append(
                    self._criar_funcionario_objeto(funcionario)
                )
            return list_funcionarios
        
    def atualizar_funcionario(self, id: int, nome: str, cpf:str, endereco:str, bairro:str, cidade:str, contato:str, data_nascimento:datetime, id_cargo:int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Funcionario).filter(Funcionario.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.cpf = cpf
                data.endereco = endereco
                data.bairro = bairro
                data.cidade = cidade
                data.contato = contato
                data.data_nascimento = data_nascimento
                data.id_cargo = id_cargo
                db_connection.session.commit()
                return self._criar_funcionario_objeto(data)
            return None

    def deletar_funcionario(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Funcionario).filter(Funcionario.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_funcionario_objeto(data)
            return data