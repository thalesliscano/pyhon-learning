from Aluno import Aluno


class Turma:
    def __init__(self, codigo, disciplina):
        self.codigo = codigo
        self.disciplina = disciplina
        self.alunos = []

    def adicionar_aluno(self, aluno:Aluno):
        if(aluno.nome and aluno.matricula):
            self.alunos.append({"aluno":aluno.nome,"matricula":aluno.matricula})
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)
        
