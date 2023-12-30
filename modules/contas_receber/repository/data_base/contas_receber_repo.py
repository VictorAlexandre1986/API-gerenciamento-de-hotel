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
            cliente=contas_receber.cliente,
            valor=contas_receber.valor,
            vencimento= contas_receber.vencimento,
            status = contas_receber.status
        )

    def criar_contas_receber(self, id: int, cliente: str, vencimento:datetime, valor:float, status:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_contas_receber = ContasReceber(id=id, cliente=cliente, vencimento=vencimento, valor=valor, status=status)
                db_connection.session.add(novo_contas_receber)
                db_connection.session.commit()
                return self._criar_receber_objeto(novo_contas_receber)
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
        
    def atualizar_contas_receber(self, id: int, cliente: str, vencimento: datetime, valor: float, status:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasReceber).filter(ContasReceber.id == id).one_or_none()
            if data:
                data.id = id
                data.cliente = cliente
                data.vencimento = vencimento
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