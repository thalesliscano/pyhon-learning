from Turma import Turma
from Aluno import Aluno

t1 = Turma("2543", "Matemática")
a1 = Aluno("Thales", "202619742")
a2 = Aluno("Roberto", "202614742")
a3 = Aluno("Richard", "202685958")

t1.adicionar_aluno(a1)
t1.adicionar_aluno(a2)
t1.adicionar_aluno(a3)
t1.listar_alunos()