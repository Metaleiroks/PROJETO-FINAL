class AlunoRepository:
    def __init__(self,db_name=""):
        self.db_name = db_name

    def listar(self):
        return self.alunos
    
    def adicionar(self, aluno):
        pass