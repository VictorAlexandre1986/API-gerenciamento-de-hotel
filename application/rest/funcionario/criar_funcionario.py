import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.funcionario.controller import FuncionarioController

api_criar_funcionario = Namespace("funcionario", description="Endpoint criar funcionario")


@api_criar_funcionario.route("/", methods=["POST"])
class CriarFuncionario(Resource):

    def post(self):
        data = api_criar_funcionario.payload
        try:
            response = FuncionarioController.criar_funcionario(data)
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