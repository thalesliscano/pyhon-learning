numero = int(input("Digite um número para calcular seu fatorial: "))

fac = 1
for i in range(numero, -1, -1):
    if(i > 0):
        fac *= i
print(f"O fatorial é: {fac}")