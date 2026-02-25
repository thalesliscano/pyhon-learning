# lambda parametros: expressao
'''
# Função normal
def dobrar(x):
    return x * 2

# Lambda equivalente
dobrar_lambda = lambda x: x * 2

print(dobrar(5))         # 10
print(dobrar_lambda(5))  # 10

############################################
exemplo de filter com for:
palavras = ["casa", "mel", "abelha", "flor", "jatai"]

ordenadas = sorted(palavras, key=lambda p: p[-1])

print(ordenadas)
'''

palavras = ["casa", "mel", "abelha", "flor", "jatai"]

odernadas = sorted(palavras, key=lambda p: p[-1].lower())

print(odernadas)


