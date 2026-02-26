from Projeto import Projeto
from Prova import Prova
from Seminario import Seminario
from Trabalho import Trabalho

avs = [
    Prova(7,10),
    Seminario(8,7),
    Trabalho(7,1.5)
]

avs1 = [
    Prova(10,10),
    Seminario(10,10),
    Trabalho(8.5,1.5)
]

for nota in avs1:
    nota.calcular_nota()
for nota in avs1:
    print(nota.resultado)
projeto = Projeto(avs1,3)
projeto.calcular_nota()
print(projeto.resultado)