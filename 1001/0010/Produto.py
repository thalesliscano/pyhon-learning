class Produto:
    def __init__(self, nome:str, preco:float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adcionar(self, qtd:int):
        if(qtd <= 0):
            print("Informe um valor maior que 0 por favor!")
        else:
            self.estoque += qtd
            print(f"Adicionado a quantidade {qtd} ao estoque!")

    def remover(self, qtd:int):
        if(qtd <= 0):
            print("Informe um valor maior que 0 por favor!")
        if(qtd > self.estoque):
            print("Valor insuciente no estoque. Informe um valor válido para retirada!")
        else:
            self.estoque -= qtd
            print(f"Removido a quantidade {qtd} do estoque!")
    def valor_total_em_estoque(self) -> float:
        valor_total = self.preco * self.estoque
        print(f"Valor total do estoque de {self.nome} é: {valor_total:.2f}")
        return valor_total
