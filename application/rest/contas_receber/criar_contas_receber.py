import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.contas_receber.controller import ContasReceberController

api_criar_contas_receber = Namespace("ContasReceber", description="Endpoint criar contas a receber")


@api_criar_contas_receber.route("/", methods=["POST"])
class CriarContaReceber(Resource):

    def post(self):
        data = api_criar_contas_receber.payload
        try:
            response = ContasReceberController.criar_contas_receber(data)
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