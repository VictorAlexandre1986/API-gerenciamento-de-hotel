import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.tipo_pagamento.controller import TipoPagamentoController

api_deletar_tipo_pagamento = Namespace("TipoPagamento", description="Endpoint deletar tipo pagamento")


@api_deletar_tipo_pagamento.route("/<int:id>", methods=["DELETE"])
class DeletarTipoPagamento(Resource):

    def delete(self, id: int):
        try:
            TipoPagamentoController.deletar_tipo_pagamento(id)
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
                status=HTTPStatus.BAD_REQUEST
            )