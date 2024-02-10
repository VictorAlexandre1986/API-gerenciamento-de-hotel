import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cliente_compra_produto.controller import ClienteCompraProdutoController

api_atualizar_cliente_compra_produto = Namespace("ClienteCompraProduto", description="Endpoint atualizar cliente compra produto")


@api_atualizar_cliente_compra_produto.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarClienteCompraProduto(Resource):

    def patch(self, id: int):
        data = api_atualizar_cliente_compra_produto.payload
        try:
            response = ClienteCompraProdutoController.atualizar_cliente_compra_produto(data,id)
            return Response(
                response.json(),
                mimetype="application/json",
                status=200,
            )

        except ValidationError as exc:
            print(exc)
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
        