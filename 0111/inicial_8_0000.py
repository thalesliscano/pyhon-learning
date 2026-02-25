# lambda parametros: expressao
'''
# Função normal
def dobrar(x):
    return x * 2

# Lambda equivalente
dobrar_lambda = lambda x: x * 2

print(dobrar(5))         # 10
print(dobrar_lambda(5))  # 10
'''

numero = int(input())

valor_triplo = lambda x: x * 3
print(valor_triplo(numero))