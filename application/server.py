from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from application.rest.login.criar_login import api_criar_login
from application.rest.login.deletar_login import api_deletar_login
from application.rest.login.buscar_login import api_buscar_login
from application.rest.login.atualizar_login import api_atualizar_login
from application.rest.reserva.criar_reserva import api_criar_reserva
from application.rest.reserva.deletar_reserva import api_deletar_reserva
from application.rest.reserva.buscar_reserva import api_buscar_reserva
from application.rest.reserva.atualizar_reserva import api_atualizar_reserva
from application.rest.funcionario.criar_funcionario import api_criar_funcionario
from application.rest.funcionario.deletar_funcionario import api_deletar_funcionario
from application.rest.funcionario.buscar_funcionario import api_buscar_funcionario
from application.rest.funcionario.atualizar_funcionario import api_atualizar_funcionario
from application.rest.contas_pagar.criar_contas_pagar import api_criar_contas_pagar
from application.rest.contas_pagar.deletar_contas_pagar import api_deletar_contas_pagar
from application.rest.contas_pagar.buscar_contas_pagar import api_buscar_contas_pagar
from application.rest.contas_pagar.atualizar_contas_pagar import api_atualizar_contas_pagar
from application.rest.contas_receber.criar_contas_receber import api_criar_contas_receber
from application.rest.contas_receber.deletar_contas_receber import api_deletar_contas_receber
from application.rest.contas_receber.buscar_contas_receber import api_buscar_contas_receber
from application.rest.contas_receber.atualizar_contas_receber import api_atualizar_contas_receber
from application.rest.produto.criar_produto import api_criar_produto
from application.rest.produto.deletar_produto import api_deletar_produto
from application.rest.produto.buscar_produto import api_buscar_produto
from application.rest.produto.atualizar_produto import api_atualizar_produto
from application.rest.tipo_pagamento.criar_tipo_pagamento import api_criar_tipo_pagamento
from application.rest.tipo_pagamento.deletar_tipo_pagamento import api_deletar_tipo_pagamento
from application.rest.tipo_pagamento.buscar_tipo_pagamento import api_buscar_tipo_pagamento
from application.rest.tipo_pagamento.atualizar_tipo_pagamento import api_atualizar_tipo_pagamento




class ServeApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self._blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

    def _init_blueprints(self, app):
        api = Api(
            self._blueprint,
            title="Forum",
            version="0.0.1",
            doc="/docs",
        )

        api.add_namespace(api_criar_login)
        api.add_namespace(api_deletar_login)
        api.add_namespace(api_atualizar_login)
        api.add_namespace(api_buscar_login)
        api.add_namespace(api_criar_reserva)
        api.add_namespace(api_deletar_reserva)
        api.add_namespace(api_atualizar_reserva)
        api.add_namespace(api_buscar_reserva)
        api.add_namespace(api_criar_funcionario)
        api.add_namespace(api_deletar_funcionario)
        api.add_namespace(api_atualizar_funcionario)
        api.add_namespace(api_buscar_funcionario)
        api.add_namespace(api_criar_contas_pagar)
        api.add_namespace(api_deletar_contas_pagar)
        api.add_namespace(api_atualizar_contas_pagar)
        api.add_namespace(api_buscar_contas_pagar)
        api.add_namespace(api_criar_contas_receber)
        api.add_namespace(api_deletar_contas_receber)
        api.add_namespace(api_atualizar_contas_receber)
        api.add_namespace(api_buscar_contas_receber)
        api.add_namespace(api_criar_produto)
        api.add_namespace(api_deletar_produto)
        api.add_namespace(api_atualizar_produto)
        api.add_namespace(api_buscar_produto)
        api.add_namespace(api_criar_tipo_pagamento)
        api.add_namespace(api_deletar_tipo_pagamento)
        api.add_namespace(api_atualizar_tipo_pagamento)
        api.add_namespace(api_buscar_tipo_pagamento)

        
        app.register_blueprint(self._blueprint)

    def create_app(self):
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)
        CORS(self.app)

        return self.app


app = ServeApplication().create_app()