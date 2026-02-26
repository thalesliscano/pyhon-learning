from Disciplina import Disciplina
from Aluno import Aluno
from Boletim import Boletim

class Turma:
    def __init__(self, disciplina:Disciplina):
        self.disciplina = disciplina
        self.alunos = []

    def matricular_aluno(self,aluno: Aluno):
        if(aluno.nome and aluno.matriula):
            self.alunos.append({"aluno":aluno.nome, "matricula":aluno.matriula})

    def criar_boletim(self, aluno:Aluno):
        aluno.boletim = Boletim()
        return aluno.boletim
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)
