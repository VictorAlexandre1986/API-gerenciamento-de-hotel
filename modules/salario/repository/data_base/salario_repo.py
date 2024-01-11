from infra.db.db_config import DBConnectionHandler
from modules.salario.repository.data_base.interface import SalarioRepositoryInterface
from modules.salario.repository.data_base.model import Salario
from modules.salario.entity import SalarioEntity
from datetime import datetime
import uuid as uuid


class SalarioRepository(SalarioRepositoryInterface):

    def _criar_salario_objeto(self, salario):
        return SalarioEntity(
            id=salario.id,
            # uuid=login.uuid,
            id_funcionario=salario.id_funcionario,
            salario=salario.salario,
            salario_status=salario.salario_status,
            vale_refeicao=salario.vale_refeicao,
            vale_refeicao_status = salario.vale_refeicao_status,
            auxilio_medico = salario.auxilio_medico,
            auxilio_medico_status = salario.auxilio_medico_status
            
        )

    def criar_salario(self, id: int, id_funcionario: int, salario:float, salario_status: bool, vale_refeicao: float, vale_refeicao_status:bool, auxilio_medico:float, auxilio_medico_status:bool):
        try:
            with DBConnectionHandler() as db_connection:
                novo_salario = Salario(id=id, id_funcionario=id_funcionario, salario=salario, salario_status=salario_status, vale_refeicao=vale_refeicao, vale_refeicao_status=vale_refeicao_status, auxilio_medico=auxilio_medico, auxilio_medico_status=auxilio_medico_status)
                db_connection.session.add(novo_salario)
                db_connection.session.commit()
                return self._criar_salario_objeto(novo_salario)
        except Exception as exc:
            raise exc

    def buscar_salario_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Salario).filter(Salario.id == id).one_or_none()
            data_resultado = self._criar_salario_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_salarios(self):
        with DBConnectionHandler() as db_connection:
            list_salarios = []
            salarios = db_connection.session.query(Salario).all()
            for salario in salarios:
                list_salarios.append(
                    self._criar_salario_objeto(salario)
                )
            return list_salarios
        
    def atualizar_salario(self, id: int,id_funcionario: int, salario:float, salario_status: bool, vale_refeicao: float, vale_refeicao_status:bool, auxilio_medico:float, auxilio_medico_status:bool):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Salario).filter(Salario.id == id).one_or_none()
            if data:
                data.id = id
                data.id_funcionario = id_funcionario
                data.salario = salario
                data.salario_status = salario_status
                data.vale_refeicao = vale_refeicao
                data.vale_refeicao_status = vale_refeicao_status
                data.auxilio_medico = auxilio_medico
                data.auxilio_medico_status=auxilio_medico_status
                db_connection.session.commit()
                return self._criar_salario_objeto(data)
            return None

    def deletar_salario(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Salario).filter(Salario.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_salario_objeto(data)
            return data