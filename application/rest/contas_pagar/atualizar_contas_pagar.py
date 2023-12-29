import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.contas_pagar.controller import ContasPagarController

api_atualizar_contas_pagar = Namespace("ContasPagar", description="Endpoint atualizar contas a pagar")


@api_atualizar_contas_pagar.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarContasPagar(Resource):

    def patch(self, id: int):
        data = api_atualizar_contas_pagar.payload
        try:
            response = ContasPagarController.atualizar_contas_pagar(data,id)
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
        