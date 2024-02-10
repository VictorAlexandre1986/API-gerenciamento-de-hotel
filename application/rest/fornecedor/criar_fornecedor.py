import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.fornecedor.controller import FornecedorController

api_criar_fornecedor = Namespace("Fornecedor", description="Endpoint criar fornecedor")


@api_criar_fornecedor.route("/", methods=["POST"])
class CriarFornecedor(Resource):

    def post(self):
        data = api_criar_fornecedor.payload
        try:
            response = FornecedorController.criar_fornecedor(data)
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