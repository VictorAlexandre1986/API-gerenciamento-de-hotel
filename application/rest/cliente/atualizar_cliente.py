import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cliente.controller import ClienteController

api_atualizar_cliente = Namespace("Cliente", description="Endpoint atualizar cliente")


@api_atualizar_cliente.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarCliente(Resource):

    def patch(self, id: int):
        data = api_atualizar_cliente.payload
        try:
            response = ClienteController.atualizar_cliente(data,id)
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
        