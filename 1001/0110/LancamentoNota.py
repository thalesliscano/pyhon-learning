class LancamentoNota:
    def __init__(self,nota, peso:float):
        self.nota = nota
        self.peso = peso
    
    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, valor):
        if(valor >= 0 and valor <= 10):
            self._nota = valor
        else:
            raise ValueError("Informe um valor entre 0 e 10!")
    
    def valor_ponderado(self):
        return self.nota * self.peso
    
    def __str__(self) -> str:
        return f"LancamentoNota(nota={self.nota}, peso={self.peso})"
    