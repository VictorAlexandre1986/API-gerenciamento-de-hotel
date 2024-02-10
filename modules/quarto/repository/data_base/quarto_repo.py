from infra.db.db_config import DBConnectionHandler
from modules.quarto.repository.data_base.interface import ProdutoRepositoryInterface
from modules.quarto.repository.data_base.model import Quarto
from modules.quarto.entity import QuartoEntity
from datetime import datetime
import uuid as uuid


class ProdutoRepository(ProdutoRepositoryInterface):

    def _criar_quarto_objeto(self, quarto):
        return QuartoEntity(
            id=produto.id,
            # uuid=login.uuid,
            tipo=produto.tipo,
            preco_aluguel=produto.preco_aluguel,
            alugado=produto.alugado,
        )

    def criar_quarto(self, id: int, tipo: str, preco_aluguel:float, alugado: bool):
        try:
            with DBConnectionHandler() as db_connection:
                novo_quuarto = Produto(id=id, tipo=tipo, preco_aluguel=preco_aluguel, alugado=alugado)
                db_connection.session.add(novo_quarto)
                db_connection.session.commit()
                return self._criar_quarto_objeto(novo_quarto)
        except Exception as exc:
            raise exc

    def buscar_produto_por_tipo(self, tipo: str):
        with DBConnectionHandler() as db_connection:
            list_quartos=[]
            quartos = db_connection.session.query(Quarto).filter(Quarto.tipo == tipo).all()
            for produto in produtos:
                list_quartos.append(
                    self._criar_quarto_objeto(quarto)
                )
            return list_quartos

    def buscar_produto_por_preco_aluguel(self, preco: float):
        with DBConnectionHandler() as db_connection:
            list_quartos=[]
            quartos = db_connection.session.query(Quarto).filter(Quarto.preco_aluguel.between(valorInicial,valorFinal)).all()
            lista_quartos = [quarto.dict() for quarto in quartos]
            return(lista_itens)
            
    def buscar_produto_por_alugado(self, alugado: bool):
        with DBConnectionHandler() as db_connection:
            list_quartos=[]
            quartos = db_connection.session.query(Quarto).filter(Quarto.alugado == alugado).all()
            for produto in produtos:
                list_quartos.append(
                    self._criar_quarto_objeto(quarto)
                )
            return list_quartos
        
    def buscar_quartos(self):
        with DBConnectionHandler() as db_connection:
            list_quartos = []
            produtos = db_connection.session.query(Quarto).all()
            for quarto in quartos:
                list_quartos.append(
                    self._criar_quarto_objeto(produto)
                )
            return list_quartos
        
    def atualizar_quarto(self, id: int, tipo: str,  preco_aluguel: float, alugado: bool):
        with DBConnectionHandler() as db_connection:
            quarto = db_connection.session.query(Quarto).filter(Quarto.id == id).one_or_none()
            if quarto:
                quarto.id = id
                quarto.tipo = tipo
                quarto.preco_aluguel = preco_aluguel
                quarto.alugado = alugado
                db_connection.session.commit()
                return self._criar_quarto_objeto(quarto)
            return None

    def deletar_quarto(self, id: int):
        with DBConnectionHandler() as db_connection:
            quarto = db_connection.session.query(Quarto).filter(Quarto.id == id).one_or_none()
            if  quarto is not None:
                db_connection.session.delete(quarto)
                db_connection.session.commit()
                return self._criar_quarto_objeto(quarto)
            return quarto