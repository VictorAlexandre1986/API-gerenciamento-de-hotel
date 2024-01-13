from modules.tipo_pagamento.dto import TipoPagamentoDTO
from modules.tipo_pagamento.repository.data_base.tipo_pagamento_repo import TipoPagamentoRepository
from modules.tipo_pagamento.usecase import TipoPagamentoUseCase



class TipoPagamentoController:

    @staticmethod
    def criar_tipo_pagamento(data: dict):
        data_dto = TipoPagamentoDTO(**data)
        repository = TipoPagamentoRepository()
        result = TipoPagamentoUseCase(repository).criar_tipo_pagamento(id = data_dto.id, tipo_pagamento= data_dto.tipo_pagamento)
        return result
    
    @staticmethod
    def buscar_tipo_pagamento_por_id(id: int):
        repository = TipoPagamentoRepository()
        result = TipoPagamentoUseCase(repository).buscar_tipo_pagamento_por_id(id)
        return result
    
    
    @staticmethod
    def buscar_tipos_pagamentos():
        repository = TipoPagamentoRepository()
        result = TipoPagamentoUseCase(repository).buscar_tipos_pagamentos()
        result = [tipo_pagamento.dict() for tipo_pagamento in result]
        return result
    
    @staticmethod
    def atualizar_tipo_pagamento(data: dict, id: int):
        data_dto = TipoPagamentoDTO(**data)
        repository = TipoPagamentoRepository()
        result = TipoPagamentoUseCase(repository).atualizar_tipo_pagamento(id = id, tipo_pagamento= data_dto.tipo_pagamento)
        return result
    
    @staticmethod
    def deletar_tipo_pagamento(id: int):
        repository = TipoPagamentoRepository()
        result = TipoPagamentoUseCase(repository).deletar_tipo_pagamento(id)
        return result