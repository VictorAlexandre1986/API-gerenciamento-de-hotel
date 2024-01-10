from infra.db.db_config import DBConnectionHandler
from modules.cargo.repository.data_base.interface import CargoRepositoryInterface
from modules.cargo.repository.data_base.model import Cargo
from modules.cargo.entity import CargoEntity
from datetime import datetime
import uuid as uuid


class CargoRepository(CargoRepositoryInterface):

    def _criar_cargo_objeto(self, cargo):
        return CargoEntity(
            id=cargo.id,
            cargo=cargo.cargo,
        )

    def criar_cargo(self, id: int, cargo: str,):
        try:
            with DBConnectionHandler() as db_connection:
                novo_cargo = Cargo(id=id, cargo=cargo)
                db_connection.session.add(novo_cargo)
                db_connection.session.commit()
                return self._criar_cargo_objeto(novo_cargo)
        except Exception as exc:
            raise exc

    def buscar_cargo_por_nome(self, nome:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cargo).filter(Cargo.nome == nome).one_or_none()
            data_resultado = self._criar_cargo_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_cargos(self):
        with DBConnectionHandler() as db_connection:
            list_cargos = []
            cargos = db_connection.session.query(Cargo).all()
            for cargo in cargos:
                list_cargos.append(
                    self._criar_cargo_objeto(cargo)
                )
            return list_cargos
        
    def atualizar_cargo(self, id: int, cargo: str, id_funcionario:int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cargo).filter(Cargo.id == id).one_or_none()
            if data:
                data.id = id
                data.cargo = cargo
                db_connection.session.commit()
                return self._criar_cargo_objeto(data)
            return None

    def deletar_cargo(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cargo).filter(Cargo.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_cargo_objeto(data)
            return data