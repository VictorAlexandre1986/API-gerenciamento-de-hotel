import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.tipo_pagamento.controller import TipoPagamentoController

api_criar_tipo_pagamento = Namespace("TipoPagamento", description="Endpoint criar tipo pagamento")


@api_criar_tipo_pagamento.route("/", methods=["POST"])
class CriarTipoPagamento(Resource):

    def post(self):
        data = api_criar_tipo_pagamento.payload
        try:
            response = TipoPagamentoController.criar_tipo_pagamento(data)
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