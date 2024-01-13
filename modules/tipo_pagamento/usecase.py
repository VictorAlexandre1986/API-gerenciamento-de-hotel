

class TipoPagamentoUseCase:
    
    def __init__(self, tipo_pagamento_repository):
        self.tipo_pagamento_repository = tipo_pagamento_repository
        
    
    def criar_contas_receber(self, id: int, tipo_pagamento: str):
        return self.tipo_pagamento_repository.criar_tipo_pagamento(id,tipo_pagamento)
    
    def buscar_tipo_pagamento_por_id(self, id: int):
        return self.tipo_pagamento_repository.buscar_tipo_pagamento_por_id(id)

    def buscar_tipos_pagamentos(self):
        return self.tipo_pagamento_repository.buscar_tipos_pagamentos()
    
    def deletar_tipo_pagamento(self, id: int):
        return self.tipo_pagamento_repository.deletar_tipo_pagamento(id)
    
    def atualizar_tipo_pagamento(self, id:int, tipo_pagamento: str):
        return self.tipo_pagamento_repository.atualizar_tipo_pagamento(id, tipo_pagamento)