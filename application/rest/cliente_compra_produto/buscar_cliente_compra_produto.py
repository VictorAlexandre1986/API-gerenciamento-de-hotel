import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cliente_compra_produto.controller import ClienteCompraProdutoController

api_buscar_cliente_compra_produto = Namespace("ClienteCompraProduto", description="Endpoint buscar cliente compra produto")


@api_buscar_cliente_compra_produto.route("/<int:id>", methods=["GET"])
class BuscarClienteCompraProdutoPorId(Resource):

    def get(self, id: int):
        try:
            response = ClienteCompraProdutoController.buscar_cliente_compra_produto_por_id(id)
            return Response(
                response.json(),
                mimetype="application/json",
                status=200,
            )

        except ValidationError as exc:
            return Response(
                exc.json(),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )


        except ValueError as exc:
            return Response(
                json.dumps({'msg': exc.args[0]}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )


        except Exception as exc:
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )
            

@api_buscar_cliente_compra_produto.route("/", methods=["GET"])
class BuscarClientesCompraProdutos(Resource):

    def get(self):
        try:
            response = ClienteCompraProdutoController.buscar_clientes_compras_produtos()
            return Response(
                json.dumps(response),
                mimetype="application/json",
                status=200,
            )

        except ValidationError as exc:
            return Response(
                exc.json(),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )

        except ValueError as exc:
            return Response(
                json.dumps({'msg': exc.args[0]}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )

        except Exception as exc:
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )
        