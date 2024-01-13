from infra.db.db_config import DBConnectionHandler
from modules.tipo_pagamento.repository.data_base.interface import TipoPagamentoRepositoryInterface
from modules.tipo_pagamento.repository.data_base.model import TipoPagamento
from modules.tipo_pagamento.entity import TipoPagamentoEntity
from datetime import datetime
import uuid as uuid


class TipoPagamentoRepository(TipoPagamentoRepositoryInterface):

    def _criar_tipo_pagamento_objeto(self, tipo_pagamento):
        return TipoPagamentoEntity(
            id=tipo_pagamento.id,
            # uuid=login.uuid,
            tipo_pagamento=tipo_pagamento.tipo_pagamento,
        )

    def criar_tipo_pagamento(self, id: int, tipo_pagamento: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_tipo_pagamento = TipoPagamento(id=id, tipo_pagamento=tipo_pagamento)
                db_connection.session.add(novo_tipo_pagamento)
                db_connection.session.commit()
                return self._criar_tipo_pagamento_objeto(novo_tipo_pagamento)
        except Exception as exc:
            raise exc

    def buscar_tipo_pagamento_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(TipoPagamento).filter(TipoPagamento.id == id).one_or_none()
            data_resultado = self._criar_tipo_pagamento_objeto(data)
            if data_resultado is not None:
                return data_resultado
             

    def buscar_tipos_pagamentos(self):
        with DBConnectionHandler() as db_connection:
            list_tipos_pagamentos = []
            tipos_pagamentos = db_connection.session.query(TipoPagamento).all()
            for tipo_pagamento in tipos_pagamentos:
                list_tipos_pagamentos.append(
                    self._criar_tipo_pagamento_objeto(tipo_pagamento)
                )
            return list_tipos_pagamentos
        
    def atualizar_tipo_pagamento(self, id: int, tipo_pagamento: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(TipoPagamento).filter(TipoPagamento.id == id).one_or_none()
            if data:
                data.id = id
                data.tipo_pagamento = tipo_pagamento
                db_connection.session.commit()
                return self._criar_tipo_pagamento_objeto(data)
            return None

    def deletar_tipo_pagamento(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(TipoPagamento).filter(TipoPagamento.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_tipo_pagamento_objeto(data)
            return data