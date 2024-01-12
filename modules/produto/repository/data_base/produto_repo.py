from infra.db.db_config import DBConnectionHandler
from modules.produto.repository.data_base.interface import ProdutoRepositoryInterface
from modules.produto.repository.data_base.model import Produto
from modules.produto.entity import ProdutoEntity
from datetime import datetime
import uuid as uuid


class ProdutoRepository(ProdutoRepositoryInterface):

    def _criar_produto_objeto(self, produto):
        return ProdutoEntity(
            id=produto.id,
            # uuid=login.uuid,
            nome=produto.nome,
            categoria=produto.categoria,
            preco_custo=produto.preco_custo,
            preco_venda = produto.preco_venda,
            id_fornecedor = produto.id_fornecedor,
            data_validade = produto.data_validade
            
        )

    def criar_produto(self, id: int, nome: str, categoria:str, preco_custo: float, preco_venda: float, id_fornecedor:int, data_validade:datetime):
        try:
            with DBConnectionHandler() as db_connection:
                novo_produto = Produto(id=id, nome=nome, categoria=categoria, preco_custo=preco_custo, preco_venda=preco_venda, id_fornecedor=id_fornecedor, data_validade=data_validade)
                db_connection.session.add(novo_produto)
                db_connection.session.commit()
                return self._criar_produto_objeto(novo_produto)
        except Exception as exc:
            raise exc

    def buscar_produto_por_nome(self, nome: str):
        with DBConnectionHandler() as db_connection:
            list_produtos=[]
            produtos = db_connection.session.query(Produto).filter(Produto.nome == nome).all()
            for produto in produtos:
                list_produtos.append(
                    self._criar_produto_objeto(produto)
                )
            return list_produtos

    def buscar_produtos(self):
        with DBConnectionHandler() as db_connection:
            list_produtos = []
            produtos = db_connection.session.query(Produto).all()
            for produto in produtos:
                list_produtos.append(
                    self._criar_produto_objeto(produto)
                )
            return list_produtos
        
    def atualizar_produto(self, id: int,nome: str, categoria:str, preco_custo: float, preco_venda: float, id_fornecedor:int, data_validade:datetime):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Produto).filter(Produto.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.categoria = categoria
                data.preco_custo = preco_custo
                data.preco_venda = preco_venda
                data.id_fornecedor = id_fornecedor
                data.data_validade = data_validade
                db_connection.session.commit()
                return self._criar_produto_objeto(data)
            return None

    def deletar_produto(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Produto).filter(Produto.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_produto_objeto(data)
            return data