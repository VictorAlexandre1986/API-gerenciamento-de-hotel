from infra.db.db_config import DBConnectionHandler
from modules.contas_receber.repository.data_base.interface import ContasReceberRepositoryInterface
from modules.contas_receber.repository.data_base.model import ContasReceber
from modules.contas_receber.entity import ContasReceberEntity
from datetime import datetime
import uuid as uuid


class ContasReceberRepository(ContasReceberRepositoryInterface):

    def _criar_contas_receber_objeto(self, contas_receber):
        return ContasReceberEntity(
            id=contas_receber.id,
            id_cliente=contas_receber.id_cliente,
            valor=contas_receber.valor,
            id_reserva = contas_receber.id_reserva,
            id_produto = contas_receber.id_produto,
            status = contas_receber.status
        )

    def criar_contas_receber(self, id: int, id_cliente: str, id_reserva:int, id_produto:int, valor:float, status:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_contas_receber = ContasReceber(id=id, id_cliente=id_cliente, id_reserva=id_reserva, id_produto=id_produto, valor=valor, status=status)
                db_connection.session.add(novo_contas_receber)
                db_connection.session.commit()
                return self._criar_contas_receber_objeto(novo_contas_receber)
        except Exception as exc:
            raise exc

    def buscar_contas_receber_por_mes(self, mes: datetime):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasReceber).filter(ContasReceber.mes == mes).one_or_none()
            data_resultado = self._criar_contas_receber_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_contas_receber(self):
        with DBConnectionHandler() as db_connection:
            list_contas_receber = []
            contas_receber = db_connection.session.query(ContasReceber).all()
            for conta_pagar in contas_receber:
                list_contas_receber.append(
                    self._criar_contas_receber_objeto(conta_pagar)
                )
            return list_contas_receber
        
    def atualizar_contas_receber(self, id: int, id_cliente: int, id_reserva: int, id_produto: int, valor: float, status:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasReceber).filter(ContasReceber.id == id).one_or_none()
            if data:
                data.id = id
                data.id_cliente = id_cliente
                data.id_reserva = id_reserva
                data.id_produto = id_produto
                data.valor = valor
                data.status = status
                db_connection.session.commit()
                return self._criar_contas_receber_objeto(data)
            return None

    def deletar_contas_receber(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasReceber).filter(ContasReceber.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_contas_receber_objeto(data)
            return data