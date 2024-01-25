from infra.db.db_config import DBConnectionHandler
from modules.reserva.repository.data_base.interface import ReservaRepositoryInterface
from modules.reserva.repository.data_base.model import Reserva
from modules.reserva.entity import ReservaEntity
from datetime import datetime
import uuid as uuid


class ReservaRepository(ReservaRepositoryInterface):

    def _criar_reserva_objeto(self, reserva):
        return ReservaEntity(
            id=reserva.id,
            # uuid=login.uuid,
            id_cliente=reserva.id_cliente,
            num_quarto=reserva.qts_quarto,
            qts_dias=reserva.qts_dias,
            data_reserva=reserva.data_reserva,
            preco = reserva.preco,
        )

    def criar_reserva(self, id: int, id_cliente: int, num_quarto:int, qts_dias: int, data_reserva: datetime, preco:float):
        try:
            with DBConnectionHandler() as db_connection:
                novo_salario = Reserva(id=id, id_cliente=id_cliente, num_quarto=num_quarto, qts_dias=qts_dias, data_reserva=data_reserva, preco=preco)
                db_connection.session.add(novo_salario)
                db_connection.session.commit()
                return self._criar_reserva_objeto(novo_salario)
        except Exception as exc:
            raise exc

    def buscar_reserva_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Reserva).filter(Reserva.id == id).one_or_none()
            data_resultado = self._criar_reserva_objeto(data)
            if data_resultado is not None:
                return data_resultado
    
    def buscar_reserva_por_data(self, inicio_mes:datetime, fim_mes:datetime):
        with DBConnectionHandler() as db_connection:
            list_reservas=[]
            reservas = db_connection.session.query(Reserva).filter(Reserva.data_reserva.between(inicio_mes,fim_mes)).all()
            for reserva in reservas:
                list_reservas.append(
                    self._criar_reserva_objeto(reserva)
                )
            return list_reservas
    
    def buscar_reserva_disponivel(self, disponivel: bool):
        with DBConnectionHandler() as db_connection:
            list_reservas=[]
            reservas = db_connection.session.query(Reserva).filter(Reserva.disponivel(disponivel=disponivel)).all()
            for reserva in reservas:
                list_reservas.append(
                    self._criar_reserva_objeto(reserva)
                )
            return list_reservas
            

    def buscar_reservas(self):
        with DBConnectionHandler() as db_connection:
            list_reservas = []
            reservas = db_connection.session.query(Reserva).all()
            for reserva in reservas:
                list_reservas.append(
                    self._criar_reserva_objeto(reserva)
                )
            return list_reservas
        
    def atualizar_reserva(self, id: int, id_cliente: int, id_quarto:int, qts_dias: int, data_reserva: datetime, preco:float):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Reserva).filter(Reserva.id == id).one_or_none()
            if data:
                data.id = id
                data.id_cliente = id_cliente
                data.id_quarto = id_quarto
                data.qts_dias = qts_dias
                data.data_reserva = data_reserva
                data.preco = preco
                db_connection.session.commit()
                return self._criar_reserva_objeto(data)
            return None

    def deletar_reserva(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Reserva).filter(Reserva.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_reserva_objeto(data)
            return data