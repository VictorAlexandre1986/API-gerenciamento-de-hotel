import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.produto.controller import SalarioController

api_criar_salario = Namespace("Salario", description="Endpoint criar salario")


@api_criar_salario.route("/", methods=["POST"])
class CriarSalario(Resource):

    def post(self):
        data = api_criar_salario.payload
        try:
            response = SalarioController.criar_salario(data)
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