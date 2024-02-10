import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.fornecedor.controller import FornecedorController

api_atualizar_fornecedor = Namespace("Fornecedor", description="Endpoint atualizar fornecedor")


@api_atualizar_fornecedor.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarFornecedor(Resource):

    def patch(self, id: int):
        data = api_atualizar_fornecedor.payload
        try:
            response = FornecedorController.atualizar_fornecedor(data,id)
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
        