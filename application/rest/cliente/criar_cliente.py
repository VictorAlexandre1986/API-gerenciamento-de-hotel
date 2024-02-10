import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cliente.controller import ClienteController

api_criar_cliente = Namespace("Cliente", description="Endpoint criar cliente")


@api_criar_cliente.route("/", methods=["POST"])
class CriarCliente(Resource):

    def post(self):
        data = api_criar_cliente.payload
        try:
            response = ClienteController.criar_cliente(data)
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