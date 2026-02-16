lista_inteiros = [2,5.66, 88, 99, 101, 2345, 123, 46, 47]
numeros_pares = []

for numero in lista_inteiros:
    if(numero % 2 != 0):
        print(f"É ímpares numero: {numero}")
    else:
        numeros_pares.append(numero)
print(f"São números pares{numeros_pares}")