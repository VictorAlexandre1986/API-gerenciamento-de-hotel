import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.fornecedor.controller import FornecedorController

api_buscar_fornecedor = Namespace("Fornecedor", description="Endpoint buscar fornecedor")

@api_buscar_fornecedor.route("/<nome:str>", methods=["GET"])
class BuscarFornecedorPorNome(Resource):

    def get(self, mes: str):
        try:
            response = FornecedorController.buscar_fornecedor_por_nome(nome)
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
            
@api_buscar_fornecedor.route("/", methods=["GET"])
class BuscarFornecedores(Resource):

    def get(self, fornecedor: str):
        try:
            response = FornecedorController.buscar_fornecedores(fornecedor)
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
            