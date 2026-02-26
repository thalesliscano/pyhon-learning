class Avaliacao:
    def __init__(self, nota):
        self.nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, valor):
        print("Estou no setter")
        if(valor >= 0 and valor <= 10):
            self._nota = valor
        else:
            raise ValueError("Valor errado")
