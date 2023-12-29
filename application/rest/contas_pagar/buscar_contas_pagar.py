import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.contas_pagar.controller import ContasPagarController

api_buscar_contas_pagar = Namespace("ContasPagar", description="Endpoint buscar contas a pagar")

@api_buscar_contas_pagar.route("/contaspagar/mes/<mes:str>", methods=["GET"])
class BuscarContaPagarPorMes(Resource):

    def get(self, mes: str):
        try:
            response = ContasPagarController.buscar_conta_pagar_por_mes(mes)
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
            
@api_buscar_contas_pagar.route("/contaspagar/fornecedor/<fornecedor:str>", methods=["GET"])
class BuscarContaPagarPorFornecedor(Resource):

    def get(self, fornecedor: str):
        try:
            response = ContasPagarController.buscar_conta_pagar_por_fornecedor(fornecedor)
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
            

@api_buscar_contas_pagar.route("/contaspagar/servico/<servico:str>", methods=["GET"])
class BuscarContaPagarPorServico(Resource):

    def get(self, servico: str):
        try:
            response = ContasPagarController.buscar_conta_pagar_por_servico(servico)
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
            

@api_buscar_contas_pagar.route("/", methods=["GET"])
class BuscarContasPagar(Resource):

    def get(self):
        try:
            response = ContasPagarController.buscar_contas_pagar()
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
        