import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.quarto.controller import QuartoController

api_criar_quarto = Namespace("Quarto", description="Endpoint criar quarto")


@api_criar_quarto.route("/", methods=["POST"])
class CriarQuarto(Resource):

    def post(self):
        data = api_criar_quarto.payload
        try:
            response = QuartoController.criar_quarto(data)
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