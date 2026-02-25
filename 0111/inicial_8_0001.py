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

numero = int(input("Digite um número: "))

eh_par = lambda x: True if x % 2 == 0 else False
print(eh_par(numero))