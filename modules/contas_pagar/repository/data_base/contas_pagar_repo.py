from infra.db.db_config import DBConnectionHandler
from modules.contas_pagar.repository.data_base.interface import ContasPagarRepositoryInterface
from modules.contas_pagar.repository.data_base.model import ContasPagar
from modules.contas_pagar.entity import ContasPagarEntity
from datetime import datetime
import uuid as uuid


class ContasPagarRepository(ContasPagarRepositoryInterface):

    def _criar_contas_pagar_objeto(self, contas_pagar):
        return ContasPagarEntity(
            id=contas_pagar.id,
            fornecedor=contas_pagar.fornecedor,
            servico=contas_pagar.servico,
            id_produto= contas_pagar.id_produto,
            valor = contas_pagar.valor,
            status = contas_pagar.status,
            data = contas_pagar.data
        )

    def criar_contas_pagar(self, id: int, fornecedor: str, servico:str, id_produto:int, valor:float, status:str, data:datetime):
        try:
            with DBConnectionHandler() as db_connection:
                novo_contas_pagar = ContasPagar(id=id, fornecedor=fornecedor, servico=servico, id_produto=id_produto, valor=valor, status=status, data=data)
                db_connection.session.add(novo_contas_pagar)
                db_connection.session.commit()
                return self._criar_pagar_objeto(novo_contas_pagar)
        except Exception as exc:
            raise exc

    def buscar_contas_pagar_por_mes(self, inicio_mes: datetime, fim_mes: datetime):
        with DBConnectionHandler() as db_connection:
            list_contas_pagar=[]
            contas_pagar = db_connection.session.query(ContasPagar).filter(ContasPagar.mes.between(inicio_mes,fim_mes)).all()
            for conta_pagar in contas_pagar:
                list_contas_pagar.append(
                    self._criar_contas_pagar_objeto(conta_pagar)
                )
            return list_contas_pagar
            
    def buscar_contas_pagar_por_fornecedor(self, fornecedor: str):
        with DBConnectionHandler() as db_connection:
            list_contas_pagar=[]
            contas_pagar = db_connection.session.query(ContasPagar).filter(ContasPagar.fornecedor == fornecedor).all()
            for conta_pagar in contas_pagar:
                list_contas_pagar.append(
                    self._criar_contas_pagar_objeto(conta_pagar)
                )
            return list_contas_pagar

    def buscar_contas_pagar_por_produto(self, produto: str):
        with DBConnectionHandler() as db_connection:
            list_contas_pagar = []
            contas_pagar = db_connection.session.query(ContasPagar).filter(ContasPagar.produto == produto).all()
            for conta_pagar in contas_pagar:
                list_contas_pagar.append(
                    self._criar_contas_pagar_objeto(conta_pagar)
                )
            return list_contas_pagar
            
    def buscar_contas_pagar_por_servico(self, servico: str):
        with DBConnectionHandler() as db_connection:
            list_contas_pagar = []
            contas_pagar = db_connection.session.query(ContasPagar).filter(ContasPagar.servico == servico).all()
            for conta_pagar in contas_pagar:
                list_contas_pagar.append(
                    self._criar_contas_pagar_objeto(conta_pagar)
                )
            return list_contas_pagar

    def buscar_contas_pagar(self):
        with DBConnectionHandler() as db_connection:
            list_contas_pagar = []
            contas_pagar = db_connection.session.query(ContasPagar).all()
            for conta_pagar in contas_pagar:
                list_contas_pagar.append(
                    self._criar_contas_pagar_objeto(conta_pagar)
                )
            return list_contas_pagar
        
    def atualizar_contas_pagar(self, id: int, fornecedor: str, servico: str, id_produto: int, valor: float, status:str, data: datetime):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasPagar).filter(ContasPagar.id == id).one_or_none()
            if data:
                data.id = id
                data.fornecedor = fornecedor
                data.servico = servico
                data.id_produto = id_produto
                data.valor = valor
                data.status = status
                data.data = data
                db_connection.session.commit()
                return self._criar_contas_pagar_objeto(data)
            return None

    def deletar_contas_pagar(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ContasPagar).filter(ContasPagar.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_contas_pagar_objeto(data)
            return data