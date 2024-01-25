import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.salario.controller import SalarioController

api_atualizar_salario = Namespace("salario", description="Endpoint atualizar salario")


@api_atualizar_salario.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarSalario(Resource):

    def patch(self, id: int):
        data = api_atualizar_salario.payload
        try:
            response = SalarioController.atualizar_salario(data,id)
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
        