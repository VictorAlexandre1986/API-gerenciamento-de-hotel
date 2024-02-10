from infra.db.db_config import DBConnectionHandler
from modules.cliente_compra_produto.repository.data_base.interface import ClienteCompraProdutoRepositoryInterface
from modules.cliente_compra_produto.repository.data_base.model import ClienteCompraProduto
from modules.cliente_compra_produto.entity import ClienteCompraProdutoEntity
from datetime import datetime
import uuid as uuid


class ClienteCompraProdutoRepository(ClienteCompraProdutoRepositoryInterface):

    def _criar_cliente_compra_produto_objeto(self, cliente_compra_produto):
        return ClienteCompraProdutoEntity(
            id=cliente_compra_produto.id,
            id_cliente=cliente_compra_produto.id_cliente,
            id_produto=cliente_compra_produto.id_produto,
            id_reserva=cliente_compra_produto.id_reserva,
            data = cliente_compra_produto.data,
            qtd = cliente_compra_produto.qtd,
        )

    def criar_cliente_compra_produto(self, id: int, id_cliente: str, id_produto:int, id_reserva:int, data:datetime, qtd: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_cliente_compra_produto = ClienteCompraProduto(id=id, id_cliente=id_cliente,  id_produto=id_produto, id_reserva=id_reserva, data=data, qtd=qtd)
                db_connection.session.add(novo_cliente_compra_produto)
                db_connection.session.commit()
                return self._criar_cliente_compra_produto_objeto(novo_cliente_compra_produto)
        except Exception as exc:
            raise exc

    def buscar_cliente_compra_produto_por_id_cliente(self, id:int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ClienteCompraProduto).filter(ClienteCompraProduto.id == id).one_or_none()
            data_resultado = self._criar_cliente_compra_produto_objeto(data)
            if data_resultado is not None:
                return data_resultado


    def buscar_clientes_compras_produtos(self):
        with DBConnectionHandler() as db_connection:
            list_cliente_compra_produto = []
            cliente_compra_produtos = db_connection.session.query(ClienteCompraProduto).all()
            for  cliente_compra_produto in cliente_compra_produtos:
                list_cliente_compra_produto.append(
                    self._criar_cliente_compra_produto_objeto(cliente_compra_produto)
                )
            return list_cliente_compra_produto
        
    def atualizar_cliente_compra_produto(self, id: int, id_cliente: int, id_produto: int, id_reserva:int, data: datetime, qtd: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ClienteCompraProduto).filter(ClienteCompraProduto.id == id).one_or_none()
            if data:
                data.id = id
                data.id_cliente = id_cliente
                data.id_produto = id_produto
                data.id_reserva = id_reserva
                data.data = data
                data.qtd = qtd
                db_connection.session.commit()
                return self._criar_contas_receber_objeto(data)
            return None

    def deletar_cliente_compra_produto(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(ClienteCompraProduto).filter(ClienteCompraProduto.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_contas_receber_objeto(data)
            return data
    

        
        