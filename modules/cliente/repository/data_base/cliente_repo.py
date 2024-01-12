from infra.db.db_config import DBConnectionHandler
from modules.cliente.repository.data_base.interface import ClienteRepositoryInterface
from modules.cliente.repository.data_base.model import Cliente
from modules.cliente.entity import ClienteEntity
from datetime import datetime
import uuid as uuid


class ClienteRepository(ClienteRepositoryInterface):

    def _criar_cliente_objeto(self, cliente):
        return ClienteEntity(
            id = cliente.id,
            nome = cliente.nome,
            cpf = cliente.cpf,
            dt_nasc = cliente.dt_nasc,
            sexo = cliente.sexo,
            endereco = cliente.endereco,
            bairro = cliente.bairro,
            cidade = cliente.cidade,
            estado = cliente.estado,
            contato = cliente.contato
        )

    def criar_cliente(self, id: int, nome: str, cpf:str, dt_nasc:datetime, sexo:str, endereco:str, bairro:str, cidade:str, estado:str, contato:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_cliente = Cliente(id=id, nome=nome, cpf=cpf, dt_nasc=dt_nasc, sexo=sexo, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, contato=contato)
                db_connection.session.add(novo_cliente)
                db_connection.session.commit()
                return self._criar_cargo_objeto(novo_cliente)
        except Exception as exc:
            raise exc

    def buscar_cliente_por_cpf(self, cpf:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cliente).filter(Cliente.cpf == cpf).one_or_none()
            data_resultado = self._criar_cargo_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_clientes(self):
        with DBConnectionHandler() as db_connection:
            list_clientes = []
            clientes = db_connection.session.query(Cliente).all()
            for cliente in clientes:
                list_clientes.append(
                    self._criar_cliente_objeto(cliente)
                )
            return list_clientes
        
    def atualizar_cliente(self, id: int,  nome: str, cpf:str, dt_nasc:datetime, sexo:str, endereco:str, bairro:str, cidade:str, estado:str, contato:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cliente).filter(Cliente.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.cpf = cpf
                data.dt_nasc = dt_nasc
                data.sexo = sexo
                data.endereco = endereco
                data.bairro = bairro
                data.cidade= cidade
                data.estado = estado
                data.contato = contato
                db_connection.session.commit()
                return self._criar_cliente_objeto(data)
            return None

    def deletar_cliente(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cliente).filter(Cliente.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_cargo_objeto(data)
            return data