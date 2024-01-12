from infra.db.db_config import DBConnectionHandler
from modules.fornecedor.repository.data_base.interface import FornecedorRepositoryInterface
from modules.fornecedor.repository.data_base.model import Fornecedor
from modules.fornecedor.entity import FornecedorEntity
from datetime import datetime
import uuid as uuid


class FornecedorRepository(FornecedorRepositoryInterface):

    def _criar_fornecedor_objeto(self, fornecedor):
        return FornecedorEntity(
            id=fornecedor.id,
            fornecedor=fornecedor.fornecedor,
            cnpj=fornecedor.cnpj,
            contato= fornecedor.contato,
        )

    def criar_fornecedor(self, id: int, fornecedor: str, cnpj:str, contato:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_fornecedor = Fornecedor(id=id, fornecedor=fornecedor, cnpj=cnpj, contato=contato)
                db_connection.session.add(novo_fornecedor)
                db_connection.session.commit()
                return self._criar_fornecedor_objeto(novo_fornecedor)
        except Exception as exc:
            raise exc


    def buscar_fornecedor_por_nome(self, fornecedor: str):
        with DBConnectionHandler() as db_connection:
            fornecedor = db_connection.session.query(Fornecedor).filter(Fornecedor.fornecedor == fornecedor).one_or_none()
            data_resultado = self._criar_fornecedor_objeto(fornecedor)
            if data_resultado is not None:
                return data_resultado

    def buscar_fornecedores(self):
        with DBConnectionHandler() as db_connection:
            list_fornecedores = []
            fornecedores = db_connection.session.query(Fornecedor).all()
            for fornecedor in fornecedores:
                list_fornecedores.append(
                    self._criar_fornecedor_objeto(fornecedor)
                )
            return list_fornecedores
        
    def atualizar_fornecedor(self, id: int, fornecedor: str, cnpj: str, contato: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Fornecedor).filter(Fornecedor.id == id).one_or_none()
            if data:
                data.id = id
                data.fornecedor = fornecedor
                data.cnpj = cnpj
                data.contato = contato
                db_connection.session.commit()
                return self._criar_fornecedor_objeto(data)
            return None

    def deletar_fornecedor(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Fornecedor).filter(Fornecedor.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_fornecedor_objeto(data)
            return data