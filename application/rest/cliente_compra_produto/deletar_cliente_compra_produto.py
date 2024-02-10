import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cliente_compra_produto.controller import ClienteCompraProdutoController

api_deletar_cliente_compra_produto = Namespace("ClienteCompraProduto", description="Endpoint deletar cliente compra produto")


@api_deletar_cliente_compra_produto.route("/<int:id>", methods=["DELETE"])
class DeletarClienteCompraProduto(Resource):

    def delete(self, id: int):
        try:
            ClienteCompraProdutoController.deletar_cliente_compra_produto(id)
            return Response(
                json.dumps({"msg": "Excluído com sucesso."}),
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