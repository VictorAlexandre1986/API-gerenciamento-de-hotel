import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.quarto.controller import QuartoController

api_deletar_quarto = Namespace("quarto", description="Endpoint deletar quarto")


@api_deletar_quarto.route("/<int:id>", methods=["DELETE"])
class DeletarQuarto(Resource):

    def delete(self, id: int):
        try:
            QuartoController.deletar_quarto(id)
            return Response(
                json.dumps({"msg": "Excluído com sucesso."}),
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
                status=HTTPStatus.BAD_REQUESsT
            )