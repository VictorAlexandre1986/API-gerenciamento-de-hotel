import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.quarto.controller import QuartoController

api_atualizar_quarto = Namespace("Quarto", description="Endpoint atualizar quarto")


@api_atualizar_quarto.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarQuarto(Resource):

    def patch(self, id: int):
        data = api_atualizar_quarto.payload
        try:
            response = QuartoController.atualizar_quarto(data,id)
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
        