import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.login.controller import LoginController

api_atualizar_reserva = Namespace("reserva", description="Endpoint atualizar reserva")


@api_atualizar_reserva.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarReserva(Resource):

    def patch(self, id: int):
        data = api_atualizar_reserva.payload
        try:
            response = ReservaController.atualizar_reserva(data,id)
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
        