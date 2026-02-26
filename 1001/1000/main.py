from Disciplina import Disciplina
from Aluno import Aluno
from Boletim import Boletim
from Turma import Turma

aluno = Aluno("Thales", "2026898")
aluno1 = Aluno("Vinicus", "2026858")

disciplina = Disciplina("Matemática", "2434")
boletim = Boletim()

turma = Turma(disciplina)
turma.matricular_aluno(aluno)
turma.matricular_aluno(aluno1)

turma.criar_boletim(aluno)
turma.criar_boletim(aluno1)

aluno.boletim.adicionar_lancamento("primeira",7,2.5)
aluno.boletim.adicionar_lancamento("primeira",4,2.5)
aluno.boletim.adicionar_lancamento("primeira",6,2.5)
aluno.boletim.adicionar_lancamento("primeira",8,2.5)

aluno.boletim.mostrar_notas()
print(aluno.boletim.media_final())

turma.listar_alunos()


