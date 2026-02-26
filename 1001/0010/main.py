from Produto import Produto

p = Produto("Caixa de leite", 5.50, 43)
p1 = Produto("Sacos de arroz", 24.00, 13)
p2 = Produto("Sacos de feijão",10.40 , 6)

p.valor_total_em_estoque()
p.remover(3)
p.valor_total_em_estoque()
p.adcionar(78)
p.valor_total_em_estoque()
p.remover(100)
p.valor_total_em_estoque()
