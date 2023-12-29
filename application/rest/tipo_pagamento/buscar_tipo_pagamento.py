import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError
from datetime import datetime

from modules.tipo_pagamento.controller import TipoPagamentoController

api_buscar_tipo_pagamento = Namespace("TipoPagamento", description="Endpoint buscar tipo pagamento")


@api_buscar_tipo_pagamento.route("/<int:id>", methods=["GET"])
class BuscarReservaPorData(Resource):

    def get(self, id: int):
        try:
            response = TipoPagamentoController.buscar_tipo_pagamento_por_id(id)
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
            

            

@api_buscar_tipo_pgamento.route("/", methods=["GET"])
class BuscarTiposPagamentos(Resource):

    def get(self):
        try:
            response = TipoPagamentoController.buscar_tipos_pagamentos()
            return Response(
                json.dumps(response),
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
        