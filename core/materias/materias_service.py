from core.materias.materias_repository import MateriaRepository
from core.materias.materias import Materias

class MateriasService:
    def __init__(self):
        self.repository = MateriaRepository()

    def listar_materias(self):    
        return self.repository.listar()
    
    def adicionar_materias(self, materias):
        if isinstance(materias, materias):
            return self.repository.adicionar(materias)
        else:
            return None
        

    def atualizar_materias(self, materias):
        if isinstance(materias, Materias):
            if materias.id > 0:
                return self.repository.atualizar(materias)
            else:
                return "ID do materias é obrigatório para atualizacão."
        else:
            return None    
        

    def remover_materias(self, materias_id):
        sucesso = self.repository.remover(materias_id)
        if not sucesso:
            return None
        else:
            return {"id":materias_id, "removido":True}
        

    def obter_materias_por_id(self, materias_id):
        materias = self.repository.obter_por_id(materias_id)
        if not materias:
            return None
        else:
            return materias    
        