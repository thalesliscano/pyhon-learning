# lambda parametros: expressao
'''
# Função normal
def dobrar(x):
    return x * 2

# Lambda equivalente
dobrar_lambda = lambda x: x * 2

print(dobrar(5))         # 10
print(dobrar_lambda(5))  # 10

#########################################
exemplo de map com for:
numeros = [1, 2, 3, 4]
dobrados = []

for n in numeros:
    dobrados.append(n * 2)

print(dobrados)
'''

numeros = [1,2,3,4,5]


lista_dobrada = list(map(lambda x: x * 2, numeros))
print(lista_dobrada)
